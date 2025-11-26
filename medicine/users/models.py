from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .validators import real_age
# AbstractUser - расширение текущей модели
# BaseAbstractUser - полное создание модели пользователя с нуля + надо определить BaseManager
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#custom-users-and-permissions


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Суперпользователь должен иметь is_superuser=True.'
            )

        return self.create_user(email, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Email',
        max_length=255,
        unique=True,
        db_index=True
    )

    first_name = models.CharField('Имя', max_length=40, blank=False)
    last_name = models.CharField('Фамилия', max_length=40, blank=False)
    middle_name = models.CharField(
        'Отчество',
        blank=True,
        max_length=40,
        help_text='Необязательное поле'
    )

    gender = models.CharField(
        'Пол',
        max_length=1,
        choices=(
            ('M', 'Мужской'),
            ('F', 'Женский'),
        ),
        blank=True
    )

    phone = models.CharField(
        'Телефон',
        max_length=20,
        unique=True,
        blank=True
    )

    date_of_birth = models.DateField(
        'Дата рождения',
        validators=(real_age,),
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email
