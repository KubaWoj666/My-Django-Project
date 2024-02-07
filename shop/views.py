from django.shortcuts import render

from core.models import Item, Category



def index_view(request):
    categories = Category.objects.all()


    context = {
         "categories": categories
    }
    return render(request, "shop/index.html", context)
