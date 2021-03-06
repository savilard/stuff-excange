# Generated by Django 3.2.7 on 2021-09-22 12:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Product slug')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('published', models.BooleanField(db_index=True, default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(db_index=True, default=0)),
                ('image', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='exchangeapp.product')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='exchangeapp.productcategory', verbose_name='Категория'),
        ),
    ]
