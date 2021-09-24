from django.urls import path

from . import views


urlpatterns = [
    path('add_product/', views.add_product, name="AddProductView"),
    path('all_products/', views.all_products, name="AllProductsView"),
]
