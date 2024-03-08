from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("categories/<slug:category_slug>/", views.category_view, name="categories"),
    path("product-detail/<uuid:item_id>/", views.detail_shop_view, name="shop-detail"),
    path("calculator", views.calculator_view, name="calculator"),
]