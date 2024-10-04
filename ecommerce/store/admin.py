from django.contrib import admin
from .models import Product, Category, Order, Review, User, CollectionPart, SlideshowImage, DiscountOffer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('review_text',)

class CollectionPartAdmin(admin.ModelAdmin):
    list_display = ('part_type', 'subtitle', 'description', 'image')
    search_fields = ('part_type', 'subtitle')

class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)

class DiscountOfferAdmin(admin.ModelAdmin):
    list_display = ('offer_text', 'link')
    search_fields = ('offer_text', 'link')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Review, ReviewAdmin)
admin.site.register(User)
admin.site.register(CollectionPart)
admin.site.register(DiscountOffer)
admin.site.register(SlideshowImage)
