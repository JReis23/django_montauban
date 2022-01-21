from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import BooleanField
from projets.models import Projets
from django.db.models import signals
from django.contrib.auth.models import User



class Checkpoints(models.Model):
    projet_checks =  models.OneToOneField(Projets, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    check1 = models.BooleanField(default='', blank=True, null=True)
    check2 = models.BooleanField(default='', blank=True, null=True)
    check3 = models.BooleanField(default='', blank=True, null=True)
    check4 = models.BooleanField(default='', blank=True, null=True)
    check5 = models.BooleanField(default='', blank=True, null=True)
    check6 = models.BooleanField(default='', blank=True, null=True)
    check7 = models.BooleanField(default='', blank=True, null=True)

    OUI = 'oui'
    NON = 'non'
    REPONSE = [
        (OUI, 'Oui'),
        (NON, 'Non')
    ]
    check8 = models.CharField(
        max_length=3,
        choices=REPONSE,
        default='', blank=True, null=True)
    check9 = models.BooleanField(default='', blank=True, null=True)
    check10 = models.BooleanField(default='', blank=True, null=True)
    check11 = models.BooleanField(default='', blank=True, null=True)
    check12 = models.BooleanField(default='', blank=True, null=True)
    check13 = models.BooleanField(default='', blank=True, null=True)
    check14 = models.BooleanField(default='', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)


    def create_checkpoints(sender, instance, created, **kwargs):
        if created:
            Checkpoints.objects.create(projet_checks = instance)    
    

    signals.post_save.connect(create_checkpoints, sender=Projets, weak=False, dispatch_uid='models.create_checkpoints')