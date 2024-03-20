from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("categories/<slug:category_slug>/", views.category_view, name="categories"),
    path("main-categories/<str:main_cat_name>/", views.main_cat_view, name="main_categories"),
    path("product-detail/<uuid:item_id>/", views.detail_shop_view, name="shop-detail"),
    path("calculator", views.calculator_view, name="calculator"),
    path("calculate-price", views.calculate_price, name="calculate_price")
]