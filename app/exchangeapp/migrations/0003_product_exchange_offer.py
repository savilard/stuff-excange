# Generated by Django 3.2.7 on 2021-09-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0002_auto_20210925_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='exchange_offer',
            field=models.CharField(db_index=True, default='default offer', max_length=50, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
