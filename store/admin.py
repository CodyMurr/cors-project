from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price',
                    'stock', 'is_available', 'created_date', 'modified_date']
    list_filter = ['is_available', 'is_active']
    list_filter = ['price', 'is_available']
    prepopulated_fields = {'slug': ('name',)}
