from django.db import models
from django.urls import reverse
from accounts.models import Account
# Create your models here.

RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING, max_length=10)
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=300)


class Product(models.Model):
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
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_date',)

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

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
