from django import views
from django.urls import path
from .views import add_to_cart, remove_from_cart

app_name = 'order'

urlpatterns = [
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart')
]