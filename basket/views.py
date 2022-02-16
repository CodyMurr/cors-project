from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from store.models import Product
from django.contrib.auth.decorators import login_required
from .basket import Basket


@login_required(login_url="/accounts/login")
def basket_summary(request):
    return render(request, 'store/basket/summary.html')


@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Basket(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('productid'))
        product = Product.objects.get(id=product_id)
        # product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    response = JsonResponse
    return redirect("home")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Basket(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Basket(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Basket(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Basket(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
