from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("categories/<slug:category_slug>/", views.category_view, name="categories")
]