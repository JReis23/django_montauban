from projets.forms import FormDevis
from django.views.generic import TemplateView
from projets.models import Projets, PhotoChantier
from django.shortcuts import get_object_or_404, render, redirect
from .models import Checkpoints
from django.contrib.auth.decorators import login_required
from .forms import CheckpointsForm
from clients.views import Clients
from projets.views import Projets
from application.filters import CheckpointsFilter, ProjetFilter

# Create your views here.
@login_required(login_url='login')
def checkpoints(request, pk):
    form_checkpoints = CheckpointsForm()
    projet_checks = Projets.objects.get(pk=pk)
    if request.method == 'POST':
        form_checkpoints = CheckpointsForm(request.POST or None)
        if form_checkpoints.is_valid():
            newchecks = form_checkpoints.save(commit=False) 
            newchecks.projet_checks = projet_checks
            newchecks.save()
        else:
            print(form_checkpoints.errors)
            form_checkpoints = CheckpointsForm()




def liste_checks(request):
    checks = Projets.objects.all()
    myFilter = ProjetFilter(request.GET, queryset=checks)
    checks = myFilter.qs
    context = {
        'checks' : checks,
        'myFilter': myFilter
    }

    return render(request, 'checkpoints.html', context)

@login_required(login_url='login')
def update_checks (request, pk):
    # photo_projet = PhotoChantier.objects.get(pk=pk)
    checks = get_object_or_404(Checkpoints, pk=pk)
    form_checkpoints = CheckpointsForm(request.POST or None, instance=checks)
    if form_checkpoints.is_valid():
        newchecks = form_checkpoints.save(commit=False)
        newchecks.checks = checks
        newchecks.modified_by = request.user
        form_checkpoints.save()

    context = {
        'form_checkpoints' : form_checkpoints,
        'checks' : checks,
        # 'photo_projet': photo_projet
    }

    return render(request, "update/update_checkpoints.html", context)


# def update_checks(request, pk):

#     checks = get_object_or_404(Checkpoints, pk=pk)
#     projet_devis = Projets.objects.get(pk=pk)

#     form_checkpoints = CheckpointsForm()
#     form_devis = FormDevis()

#     form_checkpoints = CheckpointsForm(request.POST or None, instance=checks)
#     if form_checkpoints.is_valid():
#         newchecks = form_checkpoints.save(commit=False)
#         newchecks.checks = checks
#         newchecks.modified_by = request.user
#         form_checkpoints.save()



#     form_devis = FormDevis(request.POST or None, request.FILES or None)
#     if form_devis.is_valid():
#         devis = form_devis.save(commit=False)
#         devis.projet_devis = projet_devis
#         devis.save()


#     context = {
#         'form_checkpoints' : form_checkpoints,
#         'checks' : checks, 
#         'form_devis': form_devis
#     }

#     return render(request, "update/update_checkpoints.html", context)