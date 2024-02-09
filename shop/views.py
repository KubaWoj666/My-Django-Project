from django.shortcuts import render

from core.models import Item, Category, MainCategory



def index_view(request):
     categories = Category.objects.all()

     modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     
     old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria dawna")
     
     wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")

     context = {
         "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
     }
     return render(request, "shop/index.html", context)




def shop_view(request, category_id):
     categories = Category.objects.all()

     modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     
     old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria dawna")
     
     wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")
     items = Item.objects.filter(category__id=category_id)
     
     context = {
          "items": items,
          "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
     }
     

    

     return render(request, "shop/categories.html", context)