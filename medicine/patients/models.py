from django.db import models
from django.contrib.auth import get_user_model
from .validators import check_phone, check_string_only, digits_only
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()


class Patient(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='patient'
    )

    # Полис ОМС
    oms_number = models.CharField(
        'Номер полиса ОМС',
        max_length=16,
        unique=True,
        validators=(digits_only, ),
        help_text='16 цифр нового образца'
    )

    # Контакт для экстренной связи
    emergency_contact_name = models.CharField(
        'ФИО контактного лица для экстренной связи',
        max_length=100,
        validators=(check_string_only,),
        help_text='Необязательное поле',
        blank=True,
        null=True
    )

    emergency_contact_phone = models.CharField(
        'Телефон контактного лица для экстренной связи',
        max_length=20,
        validators=(check_phone,),
        help_text='Необязательное поле',
        blank=True,
        null=True
    )

    blood_type = models.CharField(
        'Группа крови',
        max_length=3,
        choices=[
            ('0+', '0 (I) Rh+'),
            ('0-', '0 (I) Rh-'),
            ('A+', 'A (II) Rh+'),
            ('A-', 'A (II) Rh-'),
            ('B+', 'B (III) Rh+'),
            ('B-', 'B (III) Rh-'),
            ('AB+', 'AB (IV) Rh+'),
            ('AB-', 'AB (IV) Rh-'),
        ],
        blank=True,
        null=True,
        help_text='Необязательное поле'
    )

    allergies = models.TextField(
        'Аллергии',
        blank=True,
        null=True,
        help_text='Необязательное поле'
    )

    chronic_conditions = models.TextField(
        'Хронические заболевания',
        blank=True,
        null=True,
        help_text='Необязательное поле'
    )

    disability_group = models.CharField(
        'Группа инвалидности',
        max_length=5,
        blank=True,
        null=True,
        choices=[
            ('I', 'I группа'),
            ('II', 'II группа'),
            ('III', 'III группа'),
            ('Нет', 'Нет инвалидности'),
        ],
        help_text='Необязательное поле'
    )

    primary_physician = models.CharField(
        'Участковый врач',
        max_length=100,
        blank=True,
        null=True
    )

    date_created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.user.get_full_name()}'


class MedicalCard(models.Model):
    # Карта может существовать без patient - добавили вручную (адиминистратор / персонал?)
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_card',
        blank=True,
        null=True
    )

    number = models.CharField(
        'Номер медицинской карты',
        unique=True,
        max_length=20,
        help_text='Уникальный номер медицинской карты пациента'
    )

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Медицинская карта'
        verbose_name_plural = 'Медицинские карты'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.patient.user.get_full_name()} (карта {self.number})'
