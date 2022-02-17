from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from store.models import Product
from django.contrib.auth.decorators import login_required
from .models import Basket


@login_required(login_url="/accounts/login")
def basket_summary(request):
    return render(request, 'store/basket/summary.html')


@login_required(login_url="/accounts/login")
def basket_add(request, id):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
    basket.add(product=product, qty=product_qty)
    response = JsonResponse({'qty': product_qty})
    return response


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    basket = Basket(request)
    product = Product.objects.get(id=id)
    basket.remove(product)
    return redirect("basket_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    basket = Basket(request)
    product = Product.objects.get(id=id)
    basket.add(product=product)
    return redirect("basket_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    basket = Basket(request)
    product = Product.objects.get(id=id)
    basket.decrement(product=product)
    return redirect("basket_detail")


@login_required(login_url="/accounts/login")
def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect("basket_detail")


@login_required(login_url="/accounts/login")
def basket_detail(request):
    return render(request, 'basket/basket_detail.html')
