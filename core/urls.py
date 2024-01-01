from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("detail/<uuid:pk>/", views.detail_view, name="detail"),
    path("edit/<uuid:pk>/", views.edit_item_view, name="edit"),
    path("balance/", views.balance_view, name="balance"),

    path("add-category", views.create_category_view, name="add-category")

]