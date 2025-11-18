from datetime import date
from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365

    if age < 18 or age > 120:
        raise ValidationError(
            'Ожидается возраст от 18 до 120 лет'
        )
