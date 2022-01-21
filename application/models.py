from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    VALIDATEUR = 1
    CONDUCTEUR_TRAVAUX = 2
    SECRETARIAT = 3
    CHOIX_ROLE = (
        (VALIDATEUR, 'Validateur'),
        (CONDUCTEUR_TRAVAUX, 'Conducteur de Travaux'),
        (SECRETARIAT, 'Secretariat')
    )
    role = models.PositiveSmallIntegerField(choices=CHOIX_ROLE, null=True, blank=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()