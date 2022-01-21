from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import CharField
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(UserCreationForm):
    username = CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'validationCustom01'
            }
        )
    )

    password = CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'validationCustom01'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2'    
        )