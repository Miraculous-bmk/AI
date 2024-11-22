from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('arts-crafts-intl-ship', 'Arts & Crafts'),
        ('automotive-intl-ship', 'Automotive'),
        ('baby-products-intl-ship', 'Baby'),
        ('beauty-intl-ship', 'Beauty & Personal Care'),
        ('books-intl-ship', 'Books'),
        ('electronics-intl-ship', 'Computers & Electronics'),
        ('digital-music-intl-ship', 'Digital Music'),
        ('fashion-female-intl-ship', "Female's Fashion"),
        ('gift-card-intl-ship', 'Gift Card'),
        ('health-intl-ship', 'Health & Household'),
        ('kitchen-intl-ship', 'Home & Kitchen'),
        ('industrial-intl-ship', 'Industrial & Scientific'),
        ('fashion-male-intl-ship', "Male's Fashion"),
        ('movies-tv-intl-ship', 'Movies, Games & Music'),
        ('software-intl-ship', 'Software'),
        ('sporting-intl-ship', 'Sports & Outdoors'),
        ('tools-intl-ship', 'Tools & Improvement'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    product_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0) 

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ratings = self.product.ratings.all()
        self.product.rating = sum(r.rating for r in ratings) / ratings.count()
        self.product.save()

class Trend(models.Model):
    CATEGORY_CHOICES = [
        ('headphones', 'Headphones'),
        ('mens-watches', 'Men\'s Watches'),
        ('best-laptops', 'Best Laptops'),
        ('digital-cameras', 'Digital Cameras'),
        ('wireless-controllers', 'Wireless Controadmin.site.register(Collection)llers'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/trend/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FeaturedProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/featured/')

    def __str__(self):
        return self.name

class FlashSale(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/flash_sales/')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class BestSells(models.Model):
    name = models.CharField(max_length=255)
    price_now = models.DecimalField(max_digits=10, decimal_places=2)
    price_before = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="Rating should be between 0.0 and 5.0"
    )

    def __str__(self):
        return self.name
    
class Deal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/deals/')

    def __str__(self):
        return self.title

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    channels = models.CharField(max_length=255)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username