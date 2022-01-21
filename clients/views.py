from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ClientsForm
from .models import Clients
from projets.models import Projets
from django.core.paginator import Paginator
from django.db.models import Q
from application.filters import ClientFilter, ContactClientFilter

# Create your views here.


@login_required(login_url='login')
def home(request, *args, **kwargs):
    return render(request, 'home.html', {})


@login_required(login_url='login')
def recherche_all(request):
    projet = Projets.objects.all()
    if request.method == 'POST':
        searched = request.POST['searched']
        client = Clients.objects.filter(
            Q(nom_clients__icontains=searched) |
            Q(prenom_clients__icontains=searched) |
            Q(telephone_clients__icontains=searched)
        )

        return render(request, 'contact_client.html', {
            'searched': searched,
            'client': client,
            'projet': projet
        })

    else:
        return render(request, 'contact_client.html', {})


@login_required(login_url='login')
def client_info(request, pk):
    clientinfo = Clients.objects.get(pk=pk)
    client = Clients.objects.all().get(pk=pk)
    context = {
        'clientinfo': clientinfo,
        'client': client,
    }
    return render(request, 'info_client.html', context)


@login_required(login_url='login')
def client_update(request, pk):
    clientup = get_object_or_404(Clients, pk=pk)
    form = ClientsForm(request.POST or None, instance=clientup)
    if request.method == 'POST':
        form = ClientsForm(request.POST or None, request.FILES or None, instance=clientup)
        if form.is_valid():
            form.save()
            return redirect('client_info', pk=pk)

    context = {
        'form' : form,
        'clientup' : clientup
    }


    return render(request, 'update/update_client.html', context)




@login_required(login_url='login')
def client_list(request):
    client = Clients.objects.order_by('-id')
    myFilter = ClientFilter(request.GET, queryset=client)
    client = myFilter.qs

    paginator = Paginator(myFilter.qs, per_page=6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'client': client,
        'page_obj': page_obj,
        'myFilter': myFilter
    }
    return render(request, 'liste_client.html', context)


@login_required(login_url='login')
def creation_clients(request, *args, **kwargs):
    form = ClientsForm()
    if request.method == 'POST':
        form = ClientsForm(request.POST, request.FILES or None)
        if form.is_valid():
            newclient = form.save(commit=False)
            newclient.save()
            return redirect('client_list')
        else:
            form = ClientsForm()

    context = {
        'form': form
    }

    return render(request, 'creation_client.html', context)

@login_required(login_url='login')
def client_delete(request, pk):
    clientdel = get_object_or_404(Clients, pk=pk)
    if request.method == 'POST':
        clientdel.delete()
        return redirect('client_list')

    return render(request,'delete/delete.html', {})