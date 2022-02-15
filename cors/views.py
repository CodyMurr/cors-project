from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'store/home.html')


def about(request):
    return render(request, 'store/about.html')

# placed here temporarily until order category app are created


def cart(request):
    return render(request, 'store/products/cart.html')


def category(request):
    return HttpResponse('<h1>Category /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def search(request):
    return HttpResponse('<h1>Search /ᐠ｡‸｡ᐟ\ﾉ</h1>')
