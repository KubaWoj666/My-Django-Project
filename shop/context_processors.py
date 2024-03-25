from core.models import Category, Item, Image, MainCategory, MetalPrice

def category_context(request):
    categories = Category.objects.all()

    modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     
    old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Dawna")
     
    wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")

    forum_design = categories.filter(main_cat_name__main_name="Forum Design")

    context = {
         "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
          "forum_design": forum_design,
     }
    
    return context



def metal_prices_context(request):
    metal_prices = MetalPrice.objects.all().order_by("-material", "-grade")
    context = {
          "metal_prices": metal_prices,
    }

    return context