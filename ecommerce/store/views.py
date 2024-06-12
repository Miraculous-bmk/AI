from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order, Category, Review, User
from django.core.paginator import Paginator
from django.conf import settings
from web3 import Web3
import stripe


web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER_URI))
stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, 'store/home.html', )

def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "store/product.html",{'page_obj': page_obj, 'categories': categories})

@login_required
def profile(request):
    return render(request, 'store/profile.html', {'user': request.user})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/history.html', {'orders': orders})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, product=product)
    order.quantity += 1
    order.save()
    return redirect('cart')

@login_required
def cart(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'orders': orders})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

@login_required
@csrf_exempt
def checkout_session(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://your-domain.com/success/',
            cancel_url='https://your-domain.com/cancel/',
        )
        return JsonResponse({
            'id': session.id
        })
    except Exception as e:
        return HttpResponse(content=str(e), status=403)

@login_required
def crypto_payment(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    # You can add logic to generate a unique payment address for each transaction
    payment_address = 'your-crypto-wallet-address'
    context = {
        'product': product,
        'payment_address': payment_address,
        'eth_price': product.price / web3.eth.get_balance(payment_address),
    }
    return render(request, 'store/crypto_payment.html', context)

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})

def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) if query else [] # type: ignore
    return render(request, 'store/search_results.html', {'products': products, 'query': query})

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        review_text = request.POST['review_text']
        rating = request.POST['rating']
        Review.objects.create(
            product=product,
            user=request.user,
            review_text=review_text,
            rating=rating,
        )
    return redirect('product_detail', product_id=product.id)
