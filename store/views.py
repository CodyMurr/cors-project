from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator


# Create your views here.


def base(request):
    return render(request, 'store/base.html')


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'store/products/detail.html', {'product': product})


def products_all(request):
    return render(request, 'store/products/products_all.html', {'products_all': products_all})


def about(request):
    return render(request, 'store/about.html', {'about': about})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def nav_category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/includes/navbar.html', {'category': category, 'products': products})
