from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='store_users',  # Use a unique related name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='store_user_permissions',  # Use a unique related name
        blank=True,
    )

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.product.name} by {self.user.username}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"Review of {self.product.name} by {self.user.username}"

class CollectionPart(models.Model):
    PART_CHOICES = [
        ('item-big', 'Item Big'),
        ('item-slide', 'Item Slide'),
        ('item', 'Item'),
        ('item-side', 'Item Side'),
    ]
    
    part_type = models.CharField(max_length=20, choices=PART_CHOICES)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='collection_parts/', null=True, blank=True)
    slideshow_images = models.ManyToManyField('SlideshowImage', blank=True)

    def __str__(self):
        return f"{self.subtitle} - {self.part_type}"

class SlideshowImage(models.Model):
    image = models.ImageField(upload_to='slides/')
    
    def __str__(self):
        return f"Slide {self.id}"

class DiscountOffer(models.Model):
    offer_text = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title
