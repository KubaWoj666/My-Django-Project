from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("create-item/", views.create_item_view, name="create-item"),
    path("detail/<uuid:pk>/", views.detail_view, name="core-detail"),
    path("edit/<uuid:pk>/", views.edit_item_view, name="edit"),
    path("edit-metal-prices", views.edit_metal_prices, name="edit_metal_prices"),
    
    path("balance/", views.balance_view, name="balance"),

    path("add-category", views.create_category_view, name="add-category"),
    path('get-categories/', views.get_categories, name='get-categories'),

]

htmx_urlpatterns = [
    path("htmx/delete/<uuid:pk>/", views.delete_item_view, name="delete"),
]

urlpatterns += htmx_urlpatterns