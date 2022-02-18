from dataclasses import field
from pickle import FALSE
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product, Review
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView


# Create your views here.


def base(request):
    return render(request, 'store/base.html')


def home(request):
    return render(request, 'store/home.html')


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    review_form = ReviewForm()
    return render(request, 'store/products/product_detail.html', {'product': product, 'review_form': review_form})


def products_all(request):
    products = Product.objects.all()
    return render(request, 'store/products/products_all.html', {'products': products})


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


def add_review(request, slug):
    form = ReviewForm(request.POST)
    if form.is_valid():
        product = Product.objects.get(slug=slug)
        new_review = form.save(commit=False)
        new_review.product = product
        new_review.account = request.user
        new_review.save()
    return redirect('store:product_detail', slug=slug)


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = 'store:product_detail'
