from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.


# def about(request):
#     return render(request, 'store/about.html')


def base(request):
    return render(request, 'store/base.html')


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'store/products/detail.html', {'product': product})


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
