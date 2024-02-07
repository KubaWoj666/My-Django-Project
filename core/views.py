from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponse, JsonResponse

from .models import Category, Item
from .forms import ItemEditForm, CategoryForm
from sales.forms import SaleForm
from .admin import ItemResources
from django_htmx.http import HttpResponseClientRedirect




def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'



def home_view(request):
    items = Item.objects.all()

    context={
        "items": items
    }
    return render(request,  "core/home.html", context )


def detail_view(request, pk):

    item = get_object_or_404(Item, id=pk)
    sale_form = SaleForm()

    context = {
        "sale_form": sale_form,
        "item": item,
    }

    return render(request, "core/detail.html", context)

def create_item_view(request):
    form = ItemEditForm()
    category_form = CategoryForm()

    if request.method == "POST":
        form = ItemEditForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {
        "form": form,
        "category_form": category_form
    }

    return render(request, "core/create_item.html", context)


def edit_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    category_form = CategoryForm()
    
    if request.method == "POST":
        form = ItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("detail", item.id)
    else:
        form = ItemEditForm(instance=item)
    
    context = {
        "form": form,
        "item": item,
        "category_form": category_form
    }

    return render(request, "core/edit_item.html", context)


def delete_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    next_url = request.GET.get("next")

    item.delete()
    
    return HttpResponseClientRedirect(next_url)
    

def balance_view(request):
    items = Item.objects.filter(sold=False)

    if request.method == "POST":
        ids = request.POST.getlist("checkbox_items")
        if ids:
            for id in ids:
                qs = items.exclude(id=id)
        else:
            qs = items

        data_set = ItemResources().export(qs)
        format = request.POST.get("format")

        ds = data_set.xls
        response = HttpResponse(ds, content_type=f"{format}")
        response["Content-Disposition"] = f"attachment; filename=item.{format}"
        return response


    context={
        "items": items
    }
    return render(request,  "core/bilans.html", context )


def create_category_view(request):
    form = CategoryForm(request.POST or None)
    data = {}

    if is_ajax(request=request):
        if form.is_valid():
            form.save()
            data["category_name"] = form.cleaned_data.get("category_name")
            main_cat_name= form.cleaned_data.get("main_cat_name")
            print("main cat",  main_cat_name)
            data["main_category_name"] = main_cat_name.main_name

            data["status"] = 'ok'
            print(data)
            return JsonResponse(data)
    
    return JsonResponse({})


def get_categories(request):
    categories = Category.objects.all().values("id", "category_name", "main_cat_name__main_name")
    print()
    print("cat " , categories)
    return JsonResponse(list(categories), safe=False)
    




