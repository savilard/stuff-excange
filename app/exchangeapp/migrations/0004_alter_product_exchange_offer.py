# Generated by Django 3.2.7 on 2021-09-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0003_product_exchange_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='exchange_offer',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Что хочу взамен'),
        ),
    ]
