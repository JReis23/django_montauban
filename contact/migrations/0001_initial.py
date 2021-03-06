# Generated by Django 3.2.3 on 2021-06-02 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('motif_contact', models.CharField(choices=[('Reclamation', 'Reclamation'), ('Marcation de Rdv', 'Marcation de Rdv')], default='Marcation de Rdv', max_length=40)),
                ('categorie', models.CharField(default=None, max_length=40)),
                ('type_client', models.CharField(default=None, max_length=40)),
                ('date_debut', models.DateTimeField(default=None)),
                ('date_fin', models.DateTimeField(default=None)),
                ('description_contact', models.TextField(max_length=1000)),
                ('client_contact', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clients.clients')),
                ('intervenants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contact',
            },
        ),
        migrations.CreateModel(
            name='ContactValidation',
            fields=[
                ('contact_validation', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contact.contact')),
                ('valide', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
