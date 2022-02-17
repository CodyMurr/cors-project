from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_cart(request, product_id):
    cart = Order.get_cart(request.user)