from django.shortcuts import render
from .models import Category, Item


def home_view(request):
    items = Item.objects.all()

    context={
        "items": items
    }
    return render(request,  "core/home.html", context )
