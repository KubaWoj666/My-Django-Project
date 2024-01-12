from collections.abc import Iterable
from django.db import models
from core.models import Item
import uuid


class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    income = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        get_latest_by = "-created_at"

    def __str__(self):
        return self.item.name
    
    def save(self, *args, **kwargs):
        self.income =  (self.price) - (self.item.purchase_price)
        return super().save(*args, **kwargs)
    
