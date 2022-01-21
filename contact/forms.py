from django.db.models import fields
from django.forms.widgets import DateTimeInput, Select, TextInput, Textarea
from contact.models import Contact, ContactValidation
from clients.models import Clients
from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

RECLAMATION = 'Reclamation'
RDV = 'Marcation de Rdv'
sample = [
    (RECLAMATION, 'Reclamation'),
    (RDV, 'Marcation de Rdv')
]


PARTICULIER = 'Particulier'
CLIENT = 'Client'
ADMINISTRATION = 'Administration'
categories = [
    (PARTICULIER,  'Particulier'),
    (CLIENT, 'Client'),
    (ADMINISTRATION, 'Administration')
]

PROSPECT = 'Prospect'
CLIENT = 'Client'
CONTACT = 'Contact'

types_clients = [
    (PROSPECT, 'Prospect'),
    (CLIENT, 'Client'),
    (CONTACT, 'Contact')

]

class ContactForm(forms.ModelForm):
   

    motif_contact = forms.ChoiceField(
        choices=sample,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    type_client = forms.ChoiceField(
        choices=types_clients,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    categorie = forms.ChoiceField(
        choices=categories,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    date_debut = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control col-6',
                'placeholder': 'Date et heure début Rdv'
            }
        ),
        label='Date et heure début Rdv'
    )

    date_fin = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Date et heure fin Rdv'

            }
        )
    )

    description_contact = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Description demande de rdv',
                'type': 'textearea',
                'rows': 3,

            }
        )
    )

    intervenants = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': "Choisissez l'intervenant"

            }

        )
    )

    class Meta:
        model = Contact

        exclude = [
            'projet_contact',
            'client_contact'
        ]


ContactFormset = inlineformset_factory(
    Clients,
    Contact,
    form=ContactForm,
    fields=(
        'categorie',
        'type_client',
        'date_debut',
        'date_fin',
        'description_contact',
        'intervenants',


    ),
    max_num=1,
)

class ContactValidationForm(forms.ModelForm):
    class Meta:
        model = ContactValidation
        fields = ('__all__')
