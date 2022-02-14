from django.db import models
from django.urls import reverse

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField(blank=True, upload_to='products/')
    stock = models.PositiveIntegerField()

    # required

    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_date',)

    def __str__(self):
        return self.name

    REQUIRED_FIELDS = ['category', 'name',
                       'description', 'price', 'image', 'slug']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name