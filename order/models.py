import email
from email.policy import default
from django.db import models
from django.forms import BooleanField, CharField, DateTimeField, EmailField, FloatField

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey()
    order_number = CharField(max_length=20)
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    phone = CharField(max_length=11)
    email = EmailField()
    address_line_1 = CharField(max_length=50)
    address_line_2 = CharField(max_length=50)
    country = CharField(max_length=30)
    state = CharField(max_length=30)
    city = CharField(max_length=30)
    order_note = CharField(max_length=300)
    order_total = FloatField()
    tax = FloatField()
    status = CharField(max_length=30)
    is_ordered = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number