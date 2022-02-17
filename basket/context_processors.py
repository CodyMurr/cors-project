from django.shortcuts import render, redirect
from .models import Basket


def basket(request):
    return {'basket': Basket(request)}



