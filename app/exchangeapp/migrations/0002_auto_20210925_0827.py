# Generated by Django 3.2.7 on 2021-09-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='default_description', max_length=500, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
