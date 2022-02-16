from django.shortcuts import render, redirect
from .basket import Basket


def basket(request):
    return {'basket': Basket(request)}


def cart_total_amount(request):
    return render(request, 'store/basket/cart_total_amount.html')
