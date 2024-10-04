from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('setting/', views.setting, name='setting'),
    path('', views.subscribe, name='subscribe'),
]
