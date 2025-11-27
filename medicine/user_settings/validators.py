import re
from datetime import date
from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365

    if age < 14 or age > 120:
        raise ValidationError(
            'Ожидается возраст от 14 до 120 лет'
        )


def check_snils(value: str) -> None:
    pattern = r'^\d{3}-\d{3}-\d{3} \d{2}$'

    if not re.match(pattern, value):
        raise ValidationError(
            'СНИЛС должен быть в формате XXX-XXX-XXX XX'
        )


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
