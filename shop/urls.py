from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("categories/<int:category_id>/", views.shop_view, name="categories")
]