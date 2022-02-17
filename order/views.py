from django.shortcuts import redirect, render
from .models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_cart(request, product_id):
    cart = Order.get_cart(request.user)
    cart.products.add(product_id)
    return redirect('order_detail', cart)

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

