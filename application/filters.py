from django.db.models import fields
from django.forms import widgets
from django.forms.fields import ChoiceField, IntegerField
from django.forms.widgets import DateTimeInput, NumberInput, Select, SelectDateWidget, TextInput
import django_filters
from django_filters.filters import ChoiceFilter, LookupChoiceFilter, ModelChoiceFilter, NumberFilter

from .models import *
from projets.models import Projets, Entites, Devis, BonDeCommande, BonDeLivraison, PhotoChantier
from clients.models import Clients
from checkpoints.models import Checkpoints
from django_filters import DateFilter, CharFilter


class ProjetFilter(django_filters.FilterSet):
    date_debut = DateFilter(
        field_name="date_debut_projets",
        lookup_expr='gte',
        widget=DateTimeInput(
            attrs={
                'placeholder': 'Date de:',
                'class': 'col-6'
            }
        ))
    date_fin = DateFilter(
        field_name="date_debut_projets",
        lookup_expr='lte',
        widget=DateTimeInput(
            attrs={
                'placeholder': 'Date a:',
                'class': 'col-6'
            }
        ))
    titre = CharFilter(
        lookup_expr='icontains',
        field_name="nom_projets",
        label='Titre')

    numero = NumberFilter(
        field_name='id',
        widget=TextInput(
            attrs={
                'placeholder': 'Numero'
            }
        )
    )

    projet_clients = ModelChoiceFilter(
        queryset=Clients.objects.filter(),
        field_name="projet_clients",
        widget=Select(
            attrs={
                'placeholder': 'Prenom/Nom'
            }
        ))

    nom_projet = CharFilter(field_name='nom_projets',
                            lookup_expr='icontains',
                            widget=TextInput(
                                attrs={
                                    'placeholder': 'Titre'
                                }
                            )
                            )

    class Meta:
        model = Projets
        fields = (
            '__all__'
        )


class ClientFilter(django_filters.FilterSet):
    
    nom = CharFilter(
        field_name='nom_clients',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': 'Nom'
            }

        ))

    prenom = CharFilter(
        field_name='prenom_clients',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': 'Prenom'
            }

        ))

    telephone = CharFilter(
        field_name='telephone_clients',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': 'Telephone'
            }

        ))
    
    code_postal = NumberFilter(
        field_name='code_postal_clients',
        lookup_expr='icontains',
        widget=NumberInput(
            attrs={
                'placeholder': 'Code Postal'
            }

        ))

    ville = CharFilter(
        field_name='ville_clients',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': 'Ville'
            }
        )
    )

    mail = CharFilter(
        field_name='mail_clients',
        lookup_expr='icontains',
        widget=TextInput(
            attrs={
                'placeholder': 'E-mail'
            }
        )
    )

    class Meta:
        model = Clients
        fields = '__all__'
        exclude = [
            'photo_clients'
        ]


class ContactClientFilter(django_filters.FilterSet):
    

    class Meta:
        model = Clients
        fields = '__all__'
        exclude = [
            'photo_clients',
            'mail_clients',
            'date_naissance_clients',
            'adresse_clients',
            'ville_clients',
            'departement_clients',
            'code_postal_clients',
            'nom_clients'

        ]

class CheckpointsFilter(django_filters.FilterSet):

    class Meta:
        model = Checkpoints
        fields = ('__all__')