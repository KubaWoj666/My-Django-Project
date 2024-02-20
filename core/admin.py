from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export import widgets
from django.utils.html import format_html

from .models import MainCategory, Category, Item, Image
from .forms import ItemAdminForm


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



class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ["name", "category", "get_main_category_name"] #"image_tag"

    def get_main_category_name(self, obj):
        return obj.category.main_cat_name if obj.category else None
    
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" style="width: 50px"/>'.format(obj.image.url))

    # image_tag.short_description = 'Image'

    get_main_category_name.short_description = "Main Category"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "slug", )
    # prepopulated_fields = {"slug": ("category_name",)}


admin.site.register(MainCategory)
admin.site.register(Category, CategoryAdmin,)
admin.site.register(Item, ItemAdmin)
admin.site.register(Image)


