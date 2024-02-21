from django.shortcuts import render
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
     
     # get items by slug, order_by("?") = order randomly 
     items = Item.objects.filter(category__slug=category_slug).order_by("?")
     
     p = Paginator(items, 24)
     page = request.GET.get("page")
     p_items = p.get_page(page)


     context = {
          "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
          "p_items": p_items
     }
     return render(request, "shop/categories.html", context)