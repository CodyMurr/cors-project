from django.shortcuts import render
from .models import Category, Product

# Create your views here.


# def about(request):
#     return render(request, 'store/about.html')


def base(request):
    return render(request, 'store/base.html')


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
