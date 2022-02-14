from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def store(request):
    return render(request, 'store.html')

