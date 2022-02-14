from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey()
    order_note = models.CharField(max_length=300)
    order_total = models.FloatField()
    status = models.CharField(max_length=30)
    is_ordered = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.order_number

class Cart(models.Model):
    product = models.ForeignKey(on_delete=models.CASCADE)

