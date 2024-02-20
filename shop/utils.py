from django.core.paginator import Paginator


def get_paginate(obj, request):
    p = Paginator(obj, 2)
    page = request.GET.get("page")
    obj = p.get_page(page)
    print(obj)
    return obj