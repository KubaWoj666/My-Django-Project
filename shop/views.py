from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from core.models import Item, Category, MainCategory

from .utils import get_paginate



def index_view(request):
     categories = Category.objects.all()

     modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     
     old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Dawna")
     
     wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")

     print(old_jewelry)
     context = {
         "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
     }
     return render(request, "shop/index.html", context)




def category_view(request, category_slug):
     categories = Category.objects.all()
     modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Dawna")
     wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")

     item_data = []
     
     # get items by slug, order_by("?") = order randomly 
     items = Item.objects.filter(category__slug=category_slug).order_by("?")
     
     p = Paginator(items, 24)
     page = request.GET.get("page")
     p_items = p.get_page(page)
     

     for item in items:
          images = item.image_set.all()
          item_data.append({"item": item, "images": images})


     context = {
          "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
          "p_items": p_items,
          "item_data": item_data
     }
     return render(request, "shop/categories.html", context)



def detail_shop_view(request, id):
     categories = Category.objects.all()
     modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Dawna")
     wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")



     item = get_object_or_404(Item, id=id)
     images = item.image_set.all()

     context = {
          "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
          "item": item,
          "images": images
     }

     return render(request, "shop/detail_shop.html", context)
