from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "gender",
            "phone",
            "date_of_birth",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Фамилия"
            }),
            "middle_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Отчество"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+7 (___) ___-__-__",
            }),
            "date_of_birth": forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    "type": "date",
                    "class": "form-control"
                }),
        }
