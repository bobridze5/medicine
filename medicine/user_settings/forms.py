from django import forms
from django.contrib.auth import get_user_model
from .models import UserSettings

User = get_user_model()


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.require_email = kwargs.pop('require_email', False)
        super().__init__(*args, **kwargs)

        if not self.require_email:
            self.fields.pop('email')

    def clean_email(self):
        if not self.require_email:
            return None

        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError(
                'Адрес электронной почты занят другим пользователем.'
            )
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone:
            phone = phone.replace(phone[0], '7')

        if UserSettings.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                'Такой номер телефона уже используется другим пользователем.'
            )

        return phone

    class Meta:
        model = UserSettings
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "gender",
            "phone",
            "date_of_birth",
            'snils',
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Иван"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Иванов"
            }),
            "middle_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Иванович"
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
            'snils': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '123-456-789 99'
            }),
        }

        error_messages = {
            'phone': {
                'unique': "Такой номер телефона уже используется другим пользователем.",
            },
            'snils': {
                'unique': "Такой СНИЛС уже используется другим пользователем.",
            },
        }
