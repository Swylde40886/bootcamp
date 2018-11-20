from django import forms

from .models import Attendee


class AttendeeForm(forms.ModelForm):
    class Meta:

        model = Attendee
        fields = [
            'fullname',
            'email',
            'date1',
            'date2',
        ]

        widgets = {
            'fullname' : forms.TextInput(attrs={'id' : 'fullname', 'placeholder': 'Enter name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Enter email', 'class': 'form-control'}),
            'date1': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':'materialUnchecked1'}),
            'date2': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':'materialUnchecked' }),
        }
