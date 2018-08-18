from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birthdate = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birthdate', 'password1', 'password2', )

        widgets = {
            'username': TextInput(attrs={'class': 'w3-input w3-border', 'autofocus': 'True', 'required': True}),
            'birthdate': TextInput(attrs={'class': 'w3-input w3-border', 'required': True}),
            'password1': TextInput(attrs={'class': 'w3-input w3-border', 'required': True}),
            'password2': TextInput(attrs={'class': 'w3-input w3-border', 'required': True}),
        }
