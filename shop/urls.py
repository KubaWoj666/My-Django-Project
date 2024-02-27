from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("categories/<slug:category_slug>/", views.category_view, name="categories"),
    path("product-detail/<uuid:id>/", views.detail_shop_view, name="shop-detail"),
]