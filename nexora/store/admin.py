from django.contrib import admin
from .models import NewsletterSubscriber, Trend, FeaturedProduct, FlashSale, BestSells, Deal

class BestSellsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_now', 'price_before', 'rating')
    list_editable = ('rating',)

admin.site.register(BestSells, BestSellsAdmin)
admin.site.register(FeaturedProduct)
admin.site.register(FlashSale)
admin.site.register(Deal)
admin.site.register(Trend)
admin.site.register(NewsletterSubscriber)

