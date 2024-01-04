from django.db import models

import uuid

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category_name

class Item(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    inside_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    setting = models.CharField(max_length=20)
    stone = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="items", blank=True, null=True)
    certificate = models.FileField(upload_to="certificate", blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name


