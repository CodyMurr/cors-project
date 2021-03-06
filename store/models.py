from django.db import models
from django.urls import reverse
from accounts.models import Account
# Create your models here.


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField(blank=True, upload_to='images/')
    stock = models.PositiveIntegerField()

    # required

    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_date',)

    def get_absolute_url(self):
        return reverse("store:product_detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    REQUIRED_FIELDS = ['category', 'name',
                       'description', 'price', 'image', 'slug']


class Review(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    rating = models.FloatField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=300, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject
