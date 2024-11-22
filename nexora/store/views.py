from .forms import SubscriptionForm, ProductSearchForm, SignUpForm, UserProfileForm
from .models import NewsletterSubscriber, Order, Trend, FeaturedProduct, Deal
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Cart, BestSells, ProductRating
from django.utils.http import urlsafe_base64_encode 
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
from .validators import CustomPasswordValidator
from django.db.models import Q

def index(request):
    deals = Deal.objects.all()
    featured_products = FeaturedProduct.objects.all()
    best_sell = BestSells.objects.all()
    categories = Trend.objects.values_list('category', flat=True).distinct()
    grouped_products = {category: Trend.objects.filter(category=category) for category in categories}

    context = {
        'featured_products': featured_products,
        'grouped_products': grouped_products,
        'best_sell': best_sell,
        'deals': deals
    }
    return render(request, 'frontend/index.html', context)

def products(request):
    products = Product.objects.all().order_by('product_type')
    context = {
        'products': products,
    }
    return render(request, 'frontend/product.html', context)

def search(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()
    selected_category = request.GET.get('url', 'all')
    search_query = request.GET.get('field-keywords', '')

    # Filter products based on selected category and search query
    if selected_category != 'all':
        products = products.filter(category=selected_category)
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(product_type__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    context = {
        'form': form, 
        'products': products, 
        'selected_category': selected_category, 
        'query': search_query
    }
    return render(request, 'frontend/search.html', context)

def deals(request):
    return render(request, 'frontend/deals.html')

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            channels = form.cleaned_data['channels']
            
            # Save the new subscriber
            channels_str = ','.join(channels)  
            NewsletterSubscriber.objects.create(email=email, channels=channels_str)
            
            # Success message
            messages.success(request, "Thank you for subscribing!")
            return redirect('index') 
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = SubscriptionForm()

    return render(request, 'base/base.html', {'form': form})

def setting(request):
    return render(request, "base/setting.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful! You are now logged in.")
            return redirect('index')
        else:
            messages.error(request, " Signup failed. Please check your information.")
    else:
        form = SignUpForm()
    return render(request, 'profile/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user
            login= (request, user)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user}!")
                return redirect('index')
            else:
                messages.error(request, f"Invalid username or password.")
        else:
            messages.error(request, f"Login failed. Please check your information.")
    else:
        form = AuthenticationForm()
    return render(request, 'profile/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_count = sum(item.quantity for item in cart_items)
    context = {'cart_items': cart_items, 'cart_count': total_count}
    return render(request, 'frontend/cart.html', context)

@login_required
def submit_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        ProductRating.objects.update_or_create(user=request.user, product=product, defaults={'rating': rating})
    return redirect('product_detail', product_id=product.id)

@login_required
def profile(request):
    user =request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = UserProfileForm(instance=user.profile)
    return render(request, 'profile/profile.html', {'form': form})