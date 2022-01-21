from django.db.models import fields
from django.forms import widgets
from django.forms.fields import BooleanField, DateTimeField, CharField, ChoiceField, DateField, MultipleChoiceField
from django.forms.models import ModelChoiceField
from django.forms.widgets import Select
from .models import Checkpoints
from django import forms


OUI = 'oui'
NON = 'non'
REPONSE = [
    (OUI, 'Oui'),
    (NON, 'Non')
]


class CheckpointsForm(forms.ModelForm):
    check1 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check1',
                'class': 'fields',
            }
        )
    )

    check2 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check2',
                'class': 'fields',
                

            }
        )
    )

    check3 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check3',
                'class': 'fields'
            }
        )
    )

    check4 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check4',
                'class': 'fields'

            }
        )
    )

    check5 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check5',
                'class': 'fields'

            }
        )
    )

    check6 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check6',
                'class': 'fields'

            }
        )
    )

    check7 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check7',
                'class': 'fields'

            }
        )
    )

    check8 = ChoiceField(
        required=False,
        choices=REPONSE,
        widget=forms.RadioSelect(
            attrs={
                'name': 'check8',
                'class': 'form-group d-flex justify-content-between'

            }
        )
    )

    check9 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check9',
                'class': 'fields'

            }
        )
    )

    check10 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check10',
                'class': 'fields'

            }
        )
    )

    check11 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check11',
                'class': 'fields'

            }
        )
    )

    check12 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check12',
                'class': 'fields'

            }
        )
    )

    check13 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check13',
                'class': 'fields'

            }
        )
    )

    check14 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check14',
                'class': 'fields'

            }
        )
    )

    check15 = BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'check15',
                'class': 'fields'

            }
        )
    )

    class Meta:
        model = Checkpoints
        exclude = [
            'projet_checks',
            'modified_by'

        ]
