from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Specialization(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название специализации"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание специализации"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
        ordering = ['name']

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='doctor'
    )

    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.SET_NULL,  # если специализация удалена, оставляем NULL
        null=True,
        blank=False,
        related_name='doctors',
        verbose_name="Специализация"
    )

    category = models.CharField(
        max_length=50,
        verbose_name="Квалификационная категория",
        blank=True,
        null=True,
        choices=[
            ("no", "Без категории"),
            ("2", "Вторая категория"),
            ("1", "Первая категория"),
            ("top", "Высшая категория"),
        ]
    )

    medical_license_number = models.CharField(
        max_length=30,
        verbose_name="Номер медицинской лицензии",
        blank=True,
        null=True
    )

    medical_organization = models.CharField(
        max_length=255,
        verbose_name="Медицинская организация",
        blank=True,
        null=True
    )

    preview_info = models.TextField(
        verbose_name="Информация превью",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

    def __str__(self):
        return f"Доктор {self.get_full_name()} ({self.specialization})"

    def get_full_name(self):
        return self.user.settings.get_full_name()
