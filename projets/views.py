from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from .models import Entites, Projets
from .forms import *
from clients.models import Clients
from django.core.paginator import Paginator
from application.filters import ProjetFilter
from django.http import HttpResponse
from django.views import View


# from django.contrib.auth.models import User


@login_required(login_url='login')
def liste_projet(request, *args, **kwargs):
    projet = Projets.objects.order_by('-id')
    myFilter = ProjetFilter(request.GET, queryset=projet)
    projet = myFilter.qs

    paginator = Paginator(myFilter.qs, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'projet': projet,
        'page_obj': page_obj,
        'myFilter': myFilter
    }

    return render(request, 'liste_projet.html', context)


@login_required(login_url='login')
def info_projet(request, pk):
    projet = Projets.objects.get(pk=pk)
    multiple = Projets.objects.all().get(pk=pk)
    
    context = {
        'multiple': multiple,
        'projet' : projet
        
    }

    return render(request, 'info_projet.html', context)


@login_required(login_url='login')
def projet_update(request, pk):
    projetup = get_object_or_404(Projets, pk=pk)
    form = ProjetsForm(request.POST or None, instance=projetup)
    if request.method == 'POST':
        form = ProjetsForm(request.POST or None, request.FILES or None, instance=projetup)
        if form.is_valid():
            form.save()
            return redirect('info_projet', pk=pk)

    context = {
        'form' : form,
        'projetup' : projetup
    }

    return render(request, 'update_projet.html', context)


@login_required(login_url='login')
def creation_projet(request, pk):
    projet_clients = Clients.objects.get(pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form_projet = ProjetsForm(request.POST or None)
        if form_projet.is_valid():
            projets = form_projet.save(commit=False)
            projets.projet_clients = projet_clients
            projets.starter = request.user
            projets.save()
            return redirect('client_list')
    else:
        form_projet = ProjetsForm()

    context = {
        'form_projet': form_projet,
        'projet_clients': projet_clients,
    }

    return render(request, "creation_projet.html", context)



@login_required(login_url='login')
def projet_update(request, pk):
    projetup = get_object_or_404(Projets, pk=pk)
    form = ProjetsForm(request.POST or None, instance=projetup)
    if form.is_valid():
        form.save()
        return redirect('info_projet', pk=pk)
    
    context = {
        'projetup' : projetup,
        'form' : form
    }

    return render(request, 'update/update_projet.html', context)


@login_required(login_url='login')
def projet_delete(request, pk):
    projetdel = get_object_or_404(Projets, pk=pk)
    if request.method == 'POST':
        projetdel.delete()
        return redirect('liste_projet')

    return render(request,'delete/projet_delete.html', {})


@login_required(login_url='login')
def inserer_devis(request, pk):
    form_devis=FormDevis()
    projet_devis = Projets.objects.get(pk=pk)
    if request.method == 'POST':
        form_devis = FormDevis(request.POST or None, request.FILES or None)
        if form_devis.is_valid():
            devis = form_devis.save(commit=False)
            devis.projet_devis = projet_devis
            devis.save()
            return redirect('info_projet', pk=pk)

        else:
            form_devis=FormDevis()

    context = {
            'form_devis':form_devis,
            'projet_devis':projet_devis
        }

    return render(request, 'devis.html', context)


@login_required(login_url='login')
def inserer_bdc(request, pk):
    form=FormBonDeCommande()
    projet_bc = Projets.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormBonDeCommande(request.POST or None, request.FILES or None)
        if form.is_valid():
            bdc = form.save(commit=False)
            bdc.projet_bc = projet_bc
            bdc.save()
            return redirect('info_projet', pk=pk)

        else:
            form=FormBonDeCommande()


    context = {
            'form':form,
            'projet_bc':projet_bc
        }

    return render(request, 'bondecommande.html', context)


@login_required(login_url='login')
def inserer_bdl(request, pk):
    form=FormBonDeLivraison()
    projet_bl = Projets.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormBonDeLivraison(request.POST or None, request.FILES or None)
        if form.is_valid():
            bdl = form.save(commit=False)
            bdl.projet_bl = projet_bl
            bdl.save()
            return redirect('info_projet', pk=pk)

        else:
            form=FormBonDeLivraison()

    context = {
            'form':form,
            'projet_bl':projet_bl
        }

    return render(request, 'bondelivraison.html', context)

@login_required(login_url='login')
def inserer_photochantier(request, pk):
    form=FormPhotoChantier()
    projet_photo = Projets.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormPhotoChantier(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f)
            photo = form.save(commit=False)
            photo.projet_photo = projet_photo
            photo.save()
            return redirect('info_projet', pk=pk)

        else:
            form=FormPhotoChantier()

    context = {
            'form':form,
            'projet_photo':projet_photo
        }

    return render(request, 'photochantier.html', context)

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='projets/pdf')
    return None


class ViewProjetPDF(View):
    def get(self, request, pk):
        datapro = Projets.objects.get(pk=pk)
        data_dict = {
            'datapro': datapro
        }
        pdf = render_to_pdf('pdf_projet.html', data_dict)
        return HttpResponse(pdf, content_type='projets/pdf')