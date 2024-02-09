from django.db import models

import uuid


class MainCategory(models.Model):
    main_name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.main_name

class Category(models.Model):
    
    main_cat_name = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, null=True, blank=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.main_cat_name} -- {self.category_name}"

class Item(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    inside_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    setting = models.CharField(max_length=20)
    stone = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="items", default="empty_f.jpeg", blank=True, null=True)
    certificate = models.FileField(upload_to="certificate", blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


