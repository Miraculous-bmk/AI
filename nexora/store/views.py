from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import NewsletterSubscriber

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

    return render(request, 'pilar/base.html', {'form': form})

def index(request):
    return render(request, 'frontend/index.html')

def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) if query else [] # type: ignore
    return render(request, 'frontend/search.html', {'products': products, 'query': query})

def setting(request):
    return render(request, "pilar/setting.html")
