from .views import get_cached_news

def news_data(request):
    brand_news, crypto_news = get_cached_news()
    return {
        'brand_news': brand_news,
        'crypto_news': crypto_news,
    }
