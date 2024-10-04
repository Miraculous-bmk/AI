# from django.db import models

# # Create your models here.
# class CollectionPart(models.Model):
#     PART_CHOICES = [
#         ('item-big', 'Item Big'),
#         ('item-slide', 'Item Slide'),
#         ('item', 'Item'),
#         ('item-side', 'Item Side'),
#     ]
    
#     part_type = models.CharField(max_length=20, choices=PART_CHOICES)
#     total = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='collection_parts/', null=True, blank=True)
#     slideshow_images = models.ManyToManyField('SlideshowImage', blank=True)

#     def __str__(self):
#         return f"{self.total} - {self.part_type}"

# class SlideshowImage(models.Model):
#     image = models.ImageField(upload_to='slides/')
    
#     def __str__(self):
#         return f"Slide {self.id}"

# class DiscountOffer(models.Model):
#     offer_text = models.CharField(max_length=255)
#     link = models.URLField()

#     def __str__(self):
#         return self.title
