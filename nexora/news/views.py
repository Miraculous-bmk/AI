import requests
from django.core.cache import cache
from django.shortcuts import render

# API Keys
GNEWS_API_KEY = '75599d2538687a09596302152af46b44' 
CRYPTOPANIC_API_KEY = 'b9351640aad706f8810b20c55787224f7f6122c0'

def fetch_brand_news():
    url = f'https://gnews.io/api/v4/search?q=brand&token={GNEWS_API_KEY}&lang=en&max=10'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for 4xx/5xx status codes
        data = response.json()
        cache.set('brand_news', data.get('articles', []), timeout=1200)  # Cache for 20 minutes
        return data.get('articles', [])
    except requests.exceptions.RequestException as err:
        print(f"Error fetching brand news: {err}")
        # Return cached data if available
        return cache.get('brand_news', [])

def fetch_crypto_news():
    # API call to CryptoPanic with the necessary parameters
    url = f'https://cryptopanic.com/api/v1/posts/?auth_token={CRYPTOPANIC_API_KEY}&kind=news&limit=10&public=true&metadata=true&panic_score=true'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for 4xx/5xx status codes
        data = response.json()  # Parse JSON response
        print("Crypto News API Response:", data)  # Log the response for debugging
        cache.set('crypto_news', data.get('results', []), timeout=1200)  # Cache for 20 minutes
        return data.get('results', [])
    except requests.exceptions.RequestException as err:
        print(f"Error fetching crypto news: {err}")
        # Return cached data if available
        return cache.get('crypto_news', [])

def update_news_data():
    """This function fetches and updates the cache with both brand and crypto news."""
    brand_news = fetch_brand_news()
    crypto_news = fetch_crypto_news()

    # Cache the news data for 1 hour (3600 seconds)
    cache.set('brand_news', brand_news, 3600)
    cache.set('crypto_news', crypto_news, 3600)

def get_cached_news():
    """This function retrieves the news from the cache, updating it if the cache is empty."""
    brand_news = cache.get('brand_news')
    crypto_news = cache.get('crypto_news')

    # If the cache is empty, update it by fetching the latest news
    if not brand_news or not crypto_news:
        update_news_data()
        brand_news = cache.get('brand_news')
        crypto_news = cache.get('crypto_news')

    return brand_news, crypto_news

def news_view(request):
    """View function to render the news page."""
    brand_news, crypto_news = get_cached_news()  # Retrieve the cached news
    
    # Pass the news data to the template
    context = {
        'brand_news': brand_news,
        'crypto_news': crypto_news,
    }
    return render(request, 'frontend/index.html', context)
