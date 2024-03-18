from django.core.paginator import Paginator

def get_paginate(obj, request):
    p = Paginator(obj, 2)
    page = request.GET.get("page")
    obj = p.get_page(page)
    return obj


def get_images(items, item_data):
    for item in items:
        images = item.image_set.all()
        item_data.append({"item": item, "images": images})
    
    return item_data


