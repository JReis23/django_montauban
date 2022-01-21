from django.db.models import deletion
from django.utils.translation import ugettext
from clients.models import Clients
from django.db import models
from contact.models import Contact
from django.contrib.auth.models import User


from django.db.models.fields import CharField, DateField
from django.utils import timezone
# Create your models here.



# class ProjetStatus(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ATTENTE = 'En attente'
#     A_PLANIFIE = 'A planifie'
#     PLANIFIE = 'Planifie'
#     REALISES = 'Realises'
#     ETAT_PROJET = [
#         (ATTENTE, 'En attente'),
#         (A_PLANIFIE, 'A planifie'),
#         (PLANIFIE, 'Planifie'),
#         (REALISES, 'Realises')
#     ]
#     projet_status = models.CharField(
#         max_length=25, 
#         choices=ETAT_PROJET,
#         default=A_PLANIFIE
#         )

#     def __str__(self):
#         return self.projet_status 

    




class Entites(models.Model):
    id = models.BigAutoField(primary_key=True)
    MONTAUBAN = 'Montauban & Fils'
    FUNERAIRE = 'Funeraire Sud Charente'
    GAUTHIER = 'Gauthier'
    FACADE = 'Façade Sud Charente'

    CHOIX_ENTITES = [
            (MONTAUBAN, 'Montauban & Fils'),
            (FUNERAIRE, 'Funeraire Sud Charente'),
            (GAUTHIER, 'Gauthier'),
            (FACADE, 'Façade Sud Charente'),
        ]
    entites = models.CharField(
        max_length=25, 
        choices=CHOIX_ENTITES,
        default='Montauban & Fils')

    def __str__(self):
        return self.entites
    
class Projets(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_debut_projets = models.DateField(default=timezone.now)
    date_fin_provisoire = models.DateField(default=None, blank=True, null=True)
    description_projets = models.CharField(max_length=255)
    nom_projets = models.CharField(max_length=100, null=True, blank=True)
    adresse_projets = models.CharField(max_length=255)
    code_postal_projets = models.IntegerField()
    ville_projets = models.CharField(max_length=100)
    departement_projets = models.CharField(max_length=100)
    projet_clients = models.ForeignKey(Clients, on_delete=models.CASCADE, default=None)
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
    projet_status_projets =  models.CharField(
        max_length=25, 
        choices=ETAT_PROJET,
        default=A_PLANIFIE
        )
    entites_projets = models.ForeignKey(Entites, on_delete=models.CASCADE, default=None)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', default=None)

    def __str__(self):
        return self.nom_projets
    
    

class Devis(models.Model):
    id = models.BigAutoField(primary_key=True)
    titre_devis = models.CharField(max_length=255, default=None)
    numero_devis = models.CharField(max_length=20, default=None)
    date_insertion_devis = models.DateField(default=timezone.now)
    pdf_devis = models.FileField(upload_to='pdfdevis', default=None)
    projet_devis = models.ForeignKey(Projets, on_delete=models.CASCADE, default=None)
   

class BonDeCommande(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_insertion_bc = models.DateField(default=timezone.now)
    date_bc = models.DateField()
    numero_bc =  models.CharField(max_length=30, default=None)
    pdf_bc = models.FileField(upload_to='pdfbc')
    projet_bc = models.ForeignKey(Projets, on_delete=models.CASCADE, default=None)
    

class BonDeLivraison(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_insertion_bl = models.DateField(default=timezone.now)
    date_bl = models.DateField()
    numero_bl =  models.CharField(max_length=30, default=None)
    pdf_bl = models.FileField(upload_to='pdfbc')
    projet_bl = models.ForeignKey(Projets, on_delete=models.CASCADE, default=None)
    

class PhotoChantier(models.Model):
    id = models.BigAutoField(primary_key=True)
    chantier_photo = models.ImageField(upload_to='photochantier')
    projet_photo = models.ForeignKey(Projets, on_delete=models.CASCADE, default=None)






# class ProjetStatus(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     id_projets = models.ForeignKey(Projets, on_delete=models.CASCADE, default=None)



# Create your models here.
# class Checkpoints(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     checks = models.CharField(max_length=255, default=None)

#     def __str__(self):
#         return self.checks

