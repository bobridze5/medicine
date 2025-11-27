import re
from django.core.exceptions import ValidationError


def check_phone(value: str) -> None:
    pattern = r'^(7|8)\d{10}$'

    if not re.match(pattern, value):
        raise ValidationError(
            'Номер телефона должен начинаться с 7 или 8 и содержать 11 цифр'
        )


def check_string_only(value: str) -> None:
    if not value.isalpha():
        raise ValidationError(
            'Поле должно содержать только буквы'
        )


def digits_only(value):
    if not value.isdigit():
        raise ValidationError("Номер должен содержать только цифры.")
