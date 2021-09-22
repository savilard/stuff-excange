from django.contrib import admin, messages
from django.contrib.admin.decorators import action
from django.utils.translation import ngettext

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
    list_filter = ('category', 'created_at', 'published')
    search_fields = ("title__startswith", )

    list_per_page = 25

    actions = ['make_published', 'make_unpublished']

    @admin.action(description='Пометить выбранные товары как опубликованные')
    def make_published(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, ngettext(
                '%d товар был успешно отмечен как опубликованный.',
                '%d товара были успешно отмечены как опубликованные.',
                updated,
            ) % updated, messages.SUCCESS)

    @admin.action(description='Пометить выбранные товары как неопубликованные')
    def make_unpublished(self, request, queryset):
        updated = queryset.update(published=False)
        self.message_user(request, ngettext(
                '%d товар был успешно отмечен как неопубликованный.',
                '%d товара были успешно отмечены как неопубликованные.',
                updated,
            ) % updated, messages.SUCCESS)