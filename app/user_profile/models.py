from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    """Кастомный пользователь. """
    vk_link = models.CharField('Ссылка на ВКонтакте', max_length=255, blank=True)
    telegram_link = models.CharField('Ссылка на Telegram', max_length=255, blank=True)

    phonenumber = PhoneNumberField('Номер пользователя', max_length=20)

    objects = UserManager()
