from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return HttpResponse('<h1>About /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# placed here temporarily until order, store, category app are created


def store(request):
    return HttpResponse('<h1>Home /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def cart(request):
    return HttpResponse('<h1>About /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def category(request):
    return HttpResponse('<h1>Home /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def search(request):
    return HttpResponse('<h1>About /ᐠ｡‸｡ᐟ\ﾉ</h1>')
