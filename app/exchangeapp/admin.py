from django.contrib import admin

from .models import Product
from .models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'category',
        'created_at',
        'published',
    ]

    list_per_page = 25
