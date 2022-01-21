"""montauban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from application import views as application_views
from clients import views as clients_views
from projets import views as projets_views
from checkpoints import views as checkpoints_views
from chat import views as chat_views
from contact import views as contact_views
from .settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth import views as views_auth
import notifications.urls


urlpatterns = [
    path('', application_views.home, name='home'),
    path('login/', views_auth.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views_auth.LogoutView.as_view(), name='logout'),
    # path('pdf_download/', application_views.DownloadPDF.as_view(), name="pdf_download"),
    path('clients/', clients_views.client_list, name='client_list'),
    path('clients/contact', clients_views.recherche_all, name='contact'),
    path('clients/contact/new', contact_views.ClientCreateView.as_view(), name='new'),
    path('clients/contact/<int:pk>/pdf_infocontact', contact_views.ViewContactPDF.as_view(), name='pdf_infocontact'),
    path('clients/contact/<int:pk>/contact_delete', contact_views.contact_delete, name='contact_delete'),
    path('clients/<int:pk>/appele', contact_views.creation_contact, name='appele'),
    path('clients/creation_clients', clients_views.creation_clients, name='creation_clients'),
    path('clients/<int:pk>', clients_views.client_info, name='client_info'),
    path('clients/<int:pk>/pdf_infoclient/', application_views.ViewPDF.as_view(), name="pdf_infoclient"),
    path('clients/<int:pk>/creation_projet/', projets_views.creation_projet, name='creation_projet'),
    path('clients/<int:pk>/client_delete/', clients_views.client_delete, name='client_delete'),
    path('clients_update/<int:pk>', clients_views.client_update, name='clients_update'),
    path('projets/', projets_views.liste_projet, name='liste_projet'),
    path('projets_update/<int:pk>', projets_views.projet_update, name='projet_update'),
    path('projets/<int:pk>', projets_views.info_projet, name='info_projet'),
    path('projets/<int:pk>/pdf_projet', projets_views.ViewProjetPDF.as_view(), name='pdf_projet'),    
    path('projets/<int:pk>/devis', projets_views.inserer_devis, name='devis'),
    path('projets/<int:pk>/bdc', projets_views.inserer_bdc, name='bdc'),
    path('projets/<int:pk>/bdl', projets_views.inserer_bdl, name='bdl'),
    path('projets/<int:pk>/photo', projets_views.inserer_photochantier, name='photo'),
    path('projets/<int:pk>/projet_delete', projets_views.projet_delete, name='projet_delete'),
    path('projets_update/<int:pk>', projets_views.projet_update, name='projet_update'),
    path('checkpoints/', checkpoints_views.liste_checks, name='checkpoints'),
    path('checkpoints/<int:pk>', checkpoints_views.update_checks, name='update'),
    path('contact/validation', contact_views.validation_contact, name='validation'),
    path('contact/validation/<int:pk>/validation_contact', contact_views.validation_update, name='validation_contact'),

    path('chat/', chat_views.chat_send, name='chat'),
    path('chat/message', chat_views.message, name='message'),
    path('chat/read', chat_views.was_read, name='read'),
    # path('agenda', agenda_views.create_event, name='agenda'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)