from django.db.models import fields
from googleapiclient import model
from .models import *
from django import forms
from django.utils.translation import gettext_lazy as _


# class SituationProjet(forms.ModelForm):
#     projet_status = forms.ChoiceField(choices=ETAT_PROJET, required=True)


# class EntitesProjet(forms.ModelForm):
#     entites = forms.ChoiceField(choices=SOCIETES, required=True)

REPONSE = (
    ('Oui', 'Oui'),
    ('Non', 'Non')
)


ATTENTE = 'En attente'
A_PLANIFIE = 'A planifie'
PLANIFIE = 'Planifie'
REALISES = 'Realises'
ETAT_PROJET = [
        (ATTENTE, 'En attente'),
        (A_PLANIFIE, 'A planifie'),
        (PLANIFIE, 'Planifie'),
        (REALISES, 'Realises')
    ]

class ProjetsForm(forms.ModelForm):


    date_fin_provisoire = forms.DateField(
        input_formats=['%d/%m/%Y'],
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    projet_status_projets = forms.ChoiceField(
        choices=ETAT_PROJET,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    description_projets = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Description de Travaux'
    )

    nom_projets = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Nom du Projet',
    )

    entites_projets = forms.ModelChoiceField(
        queryset=Entites.objects.all(),
        label='Entites Intervenantes',
        widget=forms.Select(
            attrs={
                'class': 'form-select-control'
            }
        )
    )

    adresse_projets = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'autocomplete',
                'class': 'form-control'
            }
        ),
        label='Adresse du Projet'
    )

    code_postal_projets = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'postal_code',
                'class': 'form-control'
            }
        ),
        label='Code Postal du Projet',
    )

    ville_projets = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'locality',
                'class': 'form-control'
            }
        ),
        label='Ville du Projet'
    )

    departement_projets = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'administrative_area_level_1',
                'class': 'form-control'
            }
        ),
        label='Departement du Projet'
    )

    class Meta:
        model = Projets
        exclude = [
            'projet_clients',
            'starter',
            'date_debut_projets'

        ]


class FormDevis(forms.ModelForm):
    titre_devis = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )

    numero_devis = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )


    pdf_devis = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class' : 'form-control',
            }
        )
    )

    

    class Meta:
        model = Devis
        fields = (
            '__all__'
        )
        exclude = [
            'projet_devis',
            'date_insertion_devis'
        ]

class FormBonDeCommande(forms.ModelForm):
    class Meta:
        model = BonDeCommande
        fields = (
            '__all__'
        )
        exclude = [
            'projet_bc'
        ]

class FormBonDeLivraison(forms.ModelForm):
    class Meta:
        model = BonDeLivraison
        fields = (
            '__all__'
        )
        exclude = [
            'projet_bl'
        ]

class FormPhotoChantier(forms.ModelForm):

    chantier_photo = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple':True
            }
        )
    )

    class Meta:
        model = PhotoChantier
        fields = (
            '__all__'
        )
        exclude = [
            'projet_photo'
        ]