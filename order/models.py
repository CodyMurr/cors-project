from django.db import models
from accounts.models import Account
from store.models import Product
import uuid

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, null=True, blank=True)
    order_total = models.FloatField(null=True, blank=True)
    tax = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    is_ordered = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.order_number

    @classmethod
    def get_cart(cls, user):
        try:
            cart = cls.objects.get(user=user, is_paid=False)
        except:
            cart = cls.objects.create(user=user, order_number=uuid.uuid4().hex[:8])
        return cart

        
class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    qty = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
