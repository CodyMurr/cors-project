from django import views
from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.find_cart, name='find_cart'),
    path('orders/', views.get_orders, name='get_orders'),
]
