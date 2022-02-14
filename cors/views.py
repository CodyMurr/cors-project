from django.shortcuts import render
from django.http import HttpResponse


def store(request):
    return render(request, 'store.html')


def about(request):
    return render(request, 'about.html')

# placed here temporarily until order, store, category app are created


def cart(request):
    return render(request, 'store/cart.html')


def category(request):
    return HttpResponse('<h1>Category /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def search(request):
    return HttpResponse('<h1>Search /ᐠ｡‸｡ᐟ\ﾉ</h1>')
