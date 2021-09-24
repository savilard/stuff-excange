from django.contrib import admin, messages
from django.contrib.admin.decorators import action
from django.utils.translation import ngettext
from django.utils.html import format_html

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from .models import Product
from .models import ProductCategory
from .models import ProductImage


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'title', 'category__title', 'created_at')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['get_preview_image']
    fields = ('image', 'get_preview_image')

    def get_preview_image(self, instance):
        return format_html(
            '<img style="max-width: 200px;" src="{}"/>',
            instance.image.url,
        )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]

class ProductAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = ProductResource

    inlines = [
        ProductImageInline,
    ]
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
    readonly_fields = ('created_at',)

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

admin.site.register(Product, ProductAdmin)