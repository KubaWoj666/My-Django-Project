from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponse, JsonResponse

from .models import Category, Item, Image, MetalPrice, GoldCoin
from .forms import ItemEditForm, CategoryForm, ImageForm, GoldCoinForm
from sales.forms import SaleForm
from .admin import ItemResources
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh
from .permissions import admin_required



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@admin_required
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


@admin_required
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


@admin_required
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


@admin_required
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


@admin_required
def delete_item_view(request, pk):
    item = get_object_or_404(Item, id=pk)
    next_url = request.GET.get("next")

    item.delete()
    
    return HttpResponseClientRedirect(next_url)


@admin_required
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

@admin_required
def create_category_view(request):
    form = CategoryForm(request.POST or None)
    data = {}

    if is_ajax(request=request):
        if form.is_valid():
            form.save()
            data["category_name"] = form.cleaned_data.get("category_name")
            main_cat_name= form.cleaned_data.get("main_cat_name")

            data["main_category_name"] = main_cat_name.main_name

            data["status"] = 'ok'
           
            return JsonResponse(data)
    
    return JsonResponse({})


@admin_required
def get_categories(request):
    categories = Category.objects.all().values("id", "category_name", "main_cat_name__main_name")
    return JsonResponse(list(categories), safe=False)
    

@admin_required
def edit_metal_prices(request):
    metal_prices = MetalPrice.objects.all().order_by("-material", "-grade")

    if request.method =="POST":
        grade = request.POST.get("grade")
        new_price = request.POST.get("new_price")
        if grade and new_price:
            try:
                metal = metal_prices.get(grade=grade)
                metal.price = new_price
                metal.save()
            except MetalPrice.DoesNotExist:
                pass

    context = {
        "metal_prices": metal_prices,
    }

    return render(request, "core/edit_metal_prices.html", context)

@admin_required
def create_gold_coin(request):
    gold_coins = GoldCoin.objects.all()
    form = GoldCoinForm()

    if request.method == "POST":
        form = GoldCoinForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("gold_coin")
    
    if request.htmx:
        coin_id = request.POST.get("coin_id")
        new_price = request.POST.get("new_price")
        coin = gold_coins.get(id=coin_id)
        coin.coin_price = new_price
        coin.save()
        return HttpResponseClientRefresh()
       
        
    
    context = {
        "form": form,
        "gold_coins": gold_coins
    }
    return render(request, "core/create_gold_coin.html", context)

@admin_required
def  delete_cold_coin(request, coin_id):

    coin = get_object_or_404(GoldCoin, id=coin_id)
    coin.delete()

    gold_coins = GoldCoin.objects.all()

    context = {
        "gold_coins": gold_coins
    }

    return render(request, "core/partials/gold_coin_list.html", context)


   
