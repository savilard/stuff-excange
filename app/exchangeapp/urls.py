from django.urls import path

from . import views

urlpatterns = [
    path('add_product/', views.ProductAddView.as_view(), name="AddProductView"),
    path('all_products/', views.all_products, name="AllProductsView"),
    path('<str:username>/products/', views.UserProductsView.as_view(), name='user-products-list'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name="product-detail"),
]
