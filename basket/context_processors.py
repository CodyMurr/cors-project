from django.shortcuts import render, redirect
from .models import Basket


def basket(request):
    return {'basket': Basket(request)}


def cart_total_amount(request):
    return render(request, 'store/basket/basket_total_amount.html')
