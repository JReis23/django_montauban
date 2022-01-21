from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.db.models.fields.related import OneToOneField
from clients.models import Clients
# Create your models here.
class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    RECLAMATION = 'Reclamation'
    RDV = 'Marcation de Rdv'
    MOTIF = [
        (RECLAMATION, 'Reclamation'), 
        (RDV, 'Marcation de Rdv')
    ]
    motif_contact = models.CharField(
        max_length=40,
        choices=MOTIF,
        default=RDV,
    )
    categorie = models.CharField(default=None, max_length=40)
    type_client = models.CharField(default=None, max_length=40)
    date_debut = models.DateTimeField(default=None)
    date_fin = models.DateTimeField(default=None)
    description_contact = models.TextField(max_length=1000)
    intervenants = models.ForeignKey(User, on_delete=models.CASCADE)
    client_contact = models.ForeignKey(Clients, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'contact'



    def __str__(self):
        return self.motif_contact


class ContactValidation(models.Model):
    contact_validation = models.OneToOneField(Contact, on_delete=models.CASCADE, default=False, primary_key=True, parent_link=True)
    valide = models.BooleanField(default=False, null=True)

    def creation_contact (sender, instance, created, **kwargs):
        if created:
            ContactValidation.objects.create(contact_validation = instance)
        
    
    signals.post_save.connect(creation_contact, sender=Contact, weak=False, dispatch_uid='models.creation_contact')

