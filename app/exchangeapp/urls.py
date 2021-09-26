from django.urls import path

from . import views

urlpatterns = [
    path('add_product/', views.ProductAddView.as_view(), name="AddProductView"),
    path('all_products/', views.ProductsDisplayAllView.as_view(), name="display-all-products"),
    path('<str:username>/products/', views.UserProductsView.as_view(), name='user-products-list'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name="product-detail"),
]
