from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# AbstractUser - расширение текущей модели
# BaseAbstractUser - полное создание модели пользователя с нуля + надо определить BaseManager
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#custom-users-and-permissions


class CustomUser(AbstractUser):
