from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.text import slugify



class ProductCategory(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50, db_index=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Владелец',
        related_name='products',
        on_delete=models.CASCADE,
        default="",
    )
    title = models.CharField(verbose_name='Название', max_length=50, db_index=True)
    slug = models.SlugField(verbose_name='Product slug', max_length=100, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=500)
    exchange_offer = models.CharField(verbose_name='Что хочу взамен', max_length=50, db_index=True)
    category = models.ForeignKey(
        ProductCategory,
        verbose_name='Категория',
        related_name='products',
        null=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField('Дата регистрации', default=timezone.now, db_index=True)
    published = models.BooleanField('Опубликован', default=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title} {get_random_string(5)}')
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.slug)])


class ProductImage(models.Model):
    position = models.PositiveIntegerField(default=0, db_index=True)
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return f'{self.position} {self.product.title}'

    @property
    def get_absolute_image_url(self):
        """Get the full path to the image."""
        return f'{self.image.url}'
