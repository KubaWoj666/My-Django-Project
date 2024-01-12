from django.urls import path

from . import views

urlpatterns = [
    path("sales", views.get_all_sales_view, name="sales"),
    path("create-sale", views.create_sale_view, name="create-sale")
    

]