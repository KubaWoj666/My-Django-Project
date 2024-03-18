from django.db import models
from django.utils.text import slugify
from PIL import Image as pilImage

import uuid


class MainCategory(models.Model):
    main_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Main Categories"

    def __str__(self) -> str:
        return self.main_name

class Category(models.Model):
    slug = models.SlugField(blank=True, null=True)
    main_cat_name = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, null=True, blank=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.main_cat_name} -- {self.category_name}"
    
    def get_main_category_name(self):
        return self.main_cat_name.main_name if self.main_cat_name else None

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not set
            self.slug = slugify(f"{self.get_main_category_name()}--{self.category_name}")
        super().save(*args, **kwargs)

class Item(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    inside_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    setting = models.CharField(max_length=20)
    stone = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    certificate = models.FileField(upload_to="certificate", blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="items", default="empty_f.jpeg", blank=True, null=True)

    def __str__(self):
        return self.item.name
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # saving image first

    #     img = pilImage.open(self.image.path) # Open image using self

    #     if img.height != 900 or img.width != 900:
    #         new_img = (900, 900)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)


class MetalPrice(models.Model):
    material = models.CharField(max_length=100)
    grade = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material} - {self.grade} - {self.price} zł/g"
