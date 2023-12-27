from django.shortcuts import render, get_object_or_404

from .models import Category, Item



def home_view(request):
    items = Item.objects.all()

    context={
        "items": items
    }
    return render(request,  "core/home.html", context )


def detail_view(request, pk):

    item = get_object_or_404(Item, id=pk)

    context = {
        "item": item,
    }

    return render(request, "core/detail.html", context)

    

def balance_view(request):
    items = Item.objects.all()

    context={
        "items": items
    }
    return render(request,  "core/bilans.html", context )

