# Generated by Django 3.2.7 on 2021-09-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='Город'),
        ),
    ]
