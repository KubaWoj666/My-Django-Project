from django.contrib import admin
from import_export import resources

from .models import Category, Item


class ItemResources(resources.ModelResource):
    class Meta:
        model = Item
        fields = ["inside_number", "name", "setting", "purchase_price", "category", "created_at"]
        export_order = ["inside_number"]

admin.site.register(Category)
admin.site.register(Item)

