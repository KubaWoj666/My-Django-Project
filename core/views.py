from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Item
from .forms import ItemEditForm, CategoryForm



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


def edit_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    
    if request.method == "POST":
        form = ItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("detail", item.id)
    
    else:
        form = ItemEditForm(instance=item)
    
    context = {
        "form": form,
        "item": item
    }

    return render(request, "core/edit_item.html", context)


def create_category_view(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("edit", pk=request.POST.get("post_id"))
    