from core.models import Category, Item, Image, MainCategory

def category_context(request):
    categories = Category.objects.all()

    modern_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Współczesna") 
     
    old_jewelry = categories.filter(main_cat_name__main_name="Biżuteria Dawna")
     
    wedding_and_engagement = categories.filter(main_cat_name__main_name="Ślub i Zaręczyny")

    context = {
         "categories": categories,
          "modern_jewelry": modern_jewelry,
          "old_jewelry": old_jewelry,
          "wedding_and_engagement": wedding_and_engagement,
     }
    
    return context




    