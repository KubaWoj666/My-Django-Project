from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from core.models import Item, Image, Category, MainCategory

from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from .utils import get_paginate

import json
from django.core.serializers.json import DjangoJSONEncoder


def index_view(request):
     categories = Category.objects.all()

     modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     
     old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Dawna")
     
     wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")

     # request.session.flush()
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



def detail_shop_view(request, item_id):
     categories = Category.objects.all()
     modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Dawna")
     wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")

     recently_viewed_items_data = []
     others_items_in_category_data = []


     item = get_object_or_404(Item, id=item_id)
     images = item.image_set.all()

# Retrieving other items form same category
     category = item.category.category_name
     others_items_in_category = Item.objects.filter(category__category_name=category).exclude(id=item.id).order_by("?")[:5]
     
     for other_item in others_items_in_category:
          other_images = other_item.image_set.all()
          others_items_in_category_data.append({"other_item":other_item, "other_images": other_images})


# Retrieving if exist recently viewed items from the session.
     if "recently_viewed" in request.session:
          if item.inside_number in request.session["recently_viewed"]:
               request.session["recently_viewed"].remove(item.inside_number)

          recently_viewed_items = Item.objects.filter(inside_number__in=request.session["recently_viewed"])

          for recently_item in recently_viewed_items:
               recently_viewed_images = recently_item.image_set.all()
               recently_viewed_items_data.append({"recently_item": recently_item, "images":recently_viewed_images})        

          request.session["recently_viewed"].insert(0, item.inside_number)
          
          if len(request.session["recently_viewed"]) > 5:
               request.session["recently_viewed"].pop()
     else:
          request.session["recently_viewed"] = [item.inside_number]
     
     request.session.modified = True
     
     

     context = {
          "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
          "item": item,
          "images": images,
          "others_items_in_category_data": others_items_in_category_data,
          "recently_viewed_items_data": recently_viewed_items_data,
     }

     return render(request, "shop/detail_shop.html", context)
