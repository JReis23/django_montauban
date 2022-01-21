from django import forms
from django.contrib.auth import models
from django.db.models.fields import DateField
from django.forms.fields import CharField, EmailField, ImageField, IntegerField
from django.forms.widgets import NumberInput
from .models import Clients
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class ClientsForm(forms.ModelForm):
    nom_clients = CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'last_name',
                'class': 'form-control'
            }
        ),
        max_length=255,
        label='Nom'
    )
    prenom_clients = CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'first_name',
                'class': 'form-control'
            }
        ),
        label='Prenom'
    )
    mail_clients = EmailField(
        widget=forms.EmailInput(
            attrs={'id': 'mail',
                   'class': 'form-control'
                   }
        ),
        label='E-mail'
    )

    telephone_clients = CharField(
        widget=forms.TextInput(
            attrs={'id': 'telephone',
                   'class': 'form-control'
                   }
        ),
        label='Numero de Telephone'
    )

    photo_clients = ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    date_naissance_clients = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    adresse_clients = CharField(
        widget=forms.TextInput(
            attrs={'id': 'autocomplete',
                   'class': 'form-control'
                   }
        ),
        label='Adresse'
    )

    code_postal_clients = CharField(
        widget=forms.TextInput(
            attrs={'id': 'postal_code',
                   'class': 'form-control'
                   }
        ),
        label='Code Postal'
    )

    ville_clients = CharField(
        widget=forms.TextInput(
            attrs={'id': 'locality',
                   'class': 'form-control'
                   }
        ),
        label='Ville'
    )
    departement_clients = CharField(
        widget=forms.TextInput(
            attrs={'id': 'administrative_area_level_1',
                   'class': 'form-control'
                   }
        ),
        label='Departement'
    )
    

    class Meta:
        model = Clients
        fields = (
            '__all__'
        )




# class RawClientsForm(forms.Form):
#     nom_clients = forms.CharField(max_length=60, label='Nom Client')
