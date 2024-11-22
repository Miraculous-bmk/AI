from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('deals/', views.deals, name='deals'),
    path('login/', views.login, name='login'),
    path('sigup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('setting/', views.setting, name='setting'),
    path('profile/', views.profile, name='profile'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('application/', views.products, name='products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('submit-rating/<int:product_id>/', views.submit_rating, name='submit_rating'),
]
