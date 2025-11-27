from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    medical_record_number = forms.CharField(
        required=False,
        label="Номер медицинской карты",
    )

    first_time = forms.BooleanField(
        required=False,
        label="У меня нет карты / обращаюсь впервые"
    )

    class Meta:
        model = Patient
        fields = [
            'oms_number',
            'emergency_contact_name',
            'emergency_contact_phone',
            'blood_type',
            'allergies',
            'chronic_conditions',
            'disability_group',
        ]

        widgets = {
            'oms_number': forms.TextInput(attrs={
                'placeholder': 'Введите 16 цифр',
                'class': 'form-control',
            }),
            'emergency_contact_name': forms.TextInput(attrs={
                'placeholder': 'Иванов Иван Иванович'
            }),
            'emergency_contact_phone': forms.TextInput(attrs={
                'placeholder': '+7 (999) 999-99-99'
            }),
            'blood_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'allergies': forms.Textarea(attrs={
                'placeholder': 'Перечислите аллергии',
                'rows': 4,
                'cols': 40,
                'style': 'resize:none;'
            }),
            'chronic_conditions': forms.Textarea(attrs={
                'placeholder': 'Перечислите хронические заболевания',
                'rows': 4,
                'cols': 40,
                'style': 'resize:none;'
            }),
            'disability_group': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
