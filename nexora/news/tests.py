from django.test import TestCase
from .models import BrandNews, CryptoNews

class NewsTests(TestCase):
    def test_brand_news_model(self):
        news = BrandNews.objects.create(
            title="Test News",
            description="Test Description",
            url="http://example.com",
            published_at="2024-01-01T00:00:00Z",
            image_url="http://example.com/image.jpg"
        )
        self.assertEqual(news.title, "Test News")

    def test_crypto_news_model(self):
        news = CryptoNews.objects.create(
            title="Crypto News",
            description="Crypto Description",
            url="http://example.com",
            published_at="2024-01-01T00:00:00Z",
            image_url="http://example.com/image.jpg"
        )
        self.assertEqual(news.title, "Crypto News")
