from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponse, JsonResponse

from .models import Category, Item, Image
from .forms import ItemEditForm, CategoryForm, ImageForm
from sales.forms import SaleForm
from .admin import ItemResources
from django_htmx.http import HttpResponseClientRedirect




def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'



def home_view(request):
    items = Item.objects.all()
    item_data = []
    for item in items:
        my_item_images = item.image_set.all()
        images_urls = [image.image.url for image in my_item_images]
        item_data.append({"item": item, "images": images_urls})
    
    print(item_data)
    context={
        "items": items,
        "item_data": item_data
    }
    return render(request,  "core/home.html", context )


def detail_view(request, pk):
    images = None

    item = get_object_or_404(Item, id=pk)
    if item:
        images = item.image_set.all()
    sale_form = SaleForm()

    context = {
        "sale_form": sale_form,
        "item": item,
        "images": images
    }

    return render(request, "core/detail.html", context)

def create_item_view(request):
    form = ItemEditForm()
    category_form = CategoryForm()
    image_form = ImageForm()

    if request.method == "POST":
        form = ItemEditForm(request.POST or None)
        files = request.FILES.getlist("image")
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            for f in files:
                Image.objects.create(item=item, image=f)

            return redirect("home")
    
    context = {
        "form": form,
        "category_form": category_form,
        "image_form": image_form
    }

    return render(request, "core/create_item.html", context)


def edit_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    category_form = CategoryForm()
    image_form = ImageForm()

    images = item.image_set.all()
    
    if request.method == "POST":
        form = ItemEditForm(request.POST, instance=item)
        files = request.FILES.getlist("image")
        print("files", files)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            if len(files) != 0:
                images.delete()
                for f in files:
                    Image.objects.create(item=item, image=f)
                
            return redirect("core-detail", item.id)
    else:
        form = ItemEditForm(instance=item)
    
    context = {
        "item": item,
        "images": images,
        "form": form,
        "image_form": image_form,
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
    item_data = []

    for item in items:
        my_item_images = item.image_set.all()
        images_urls = [image.image.url for image in my_item_images]
        item_data.append({"item": item, "images": images_urls})

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
        "item_data_list": item_data
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
    return JsonResponse(list(categories), safe=False)
    




