from django.db import models


class Clients(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_clients = models.CharField(max_length=100)
    prenom_clients = models.CharField(max_length=100)
    mail_clients = models.EmailField(null=True, blank=True)
    telephone_clients = models.CharField(max_length=20)
    photo_clients = models.ImageField(upload_to='images', default='/static/img/avatar.png', null=True)
    date_naissance_clients = models.DateField(blank=True, null=True)
    adresse_clients = models.CharField(max_length=255, default=None, null=True, blank=True)
    ville_clients = models.CharField(max_length=100, null=True, blank=True)
    departement_clients = models.CharField(max_length=100, null=True, blank=True)
    code_postal_clients = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'clients'

    def __str__(self):
        return self.nom_clients


