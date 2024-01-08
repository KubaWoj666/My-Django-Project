from django.urls import path
from . import views

# app_name = "core"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("create-item/", views.create_item_view, name="create-item"),
    path("detail/<uuid:pk>/", views.detail_view, name="detail"),
    path("edit/<uuid:pk>/", views.edit_item_view, name="edit"),
    
    path("balance/", views.balance_view, name="balance"),

    path("add-category", views.create_category_view, name="add-category"),
    path('get-categories/', views.get_categories, name='get-categories'),

    path("test/", views.PostListView.as_view(), name="test"),

]

htmx_urlpatterns = [
    path("htmx/delete/<uuid:pk>/", views.delete_item_view, name="delete"),
]

urlpatterns += htmx_urlpatterns