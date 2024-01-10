from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export import widgets

from .models import Category, Item


class ItemResources(resources.ModelResource):
    category = Field()
    created_at = Field() 
    class Meta:
        model = Item
        fields = ["inside_number", "name", "setting", "purchase_price", "category", "created_at"]
        export_order = ["inside_number", "name", "setting", "purchase_price", "category", "created_at"]
    
    def dehydrate_category(self, obj):
        return obj.category.category_name
    
    def dehydrate_created_at(self, obj):
        return obj.created_at.strftime("%d-%m-%Y")

admin.site.register(Category)
admin.site.register(Item)

