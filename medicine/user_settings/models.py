from django.db import models
from django.contrib.auth import get_user_model
from .validators import real_age, check_snils, check_phone, check_string_only

User = get_user_model()


class UserSettings(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='settings'
    )

    first_name = models.CharField(
        'Имя',
        max_length=40,
        blank=False,
        validators=(check_string_only,)
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=40,
        blank=False,
        validators=(check_string_only,)
    )
    middle_name = models.CharField(
        'Отчество',
        blank=True,
        max_length=40,
        help_text='Необязательное поле',
        validators=(check_string_only,)
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

    snils = models.CharField(
        max_length=14,
        unique=True,
        verbose_name="СНИЛС",
        validators=(check_snils,)
    )

    phone = models.CharField(
        'Телефон',
        max_length=20,
        unique=True,
        blank=True,
        validators=(check_phone,)
    )

    date_of_birth = models.DateField(
        'Дата рождения',
        validators=(real_age,),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Настройки пользователя {self.user.email}'

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
