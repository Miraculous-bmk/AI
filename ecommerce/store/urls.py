from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('signup/', views.signup, name='signup'),
    path('order-history/', views.order_history, name='order_history'),
    path('search/', views.search, name='search'),
    path('product/', views.product, name='product'),
    path('setting/', views.setting, name='setting'),
    path('collection/', views.collection_view, name='collection_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout-session/<int:product_id>/', views.checkout_session, name='checkout_session'),
    path('crypto-payment/<int:product_id>/', views.crypto_payment, name='crypto_payment'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('add-review/<int:product_id>/', views.add_review, name='add_review'),
]
