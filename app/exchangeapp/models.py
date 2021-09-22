from django.db import models
from django.utils import timezone


class ProductCategory(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50, db_index=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50, db_index=True)
    slug = models.SlugField(verbose_name='Product slug', max_length=100, unique=True)
    category = models.ForeignKey(
        ProductCategory,
        verbose_name='Категория',
        related_name='products',
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField('Дата регистрации', default=timezone.now, db_index=True)
    published = models.BooleanField('Опубликован', default=True, db_index=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.title
