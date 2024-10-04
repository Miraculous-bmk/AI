from django.contrib import admin
from .models import CollectionPart, SlideshowImage, DiscountOffer


# Register your models here.
admin.site.register(CollectionPart)
class CollectionPartAdmin(admin.ModelAdmin):
    list_display = ('part_type', 'subtitle', 'description', 'image')
    search_fields = ('part_type', 'subtitle')

admin.site.register(SlideshowImage)
class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)

admin.site.register(DiscountOffer)
class DiscountOfferAdmin(admin.ModelAdmin):
    list_display = ('offer_text', 'link')
    search_fields = ('offer_text', 'link')
