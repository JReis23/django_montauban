from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.checks.messages import Error
from django.shortcuts import get_object_or_404, redirect, render
from .models import Contact, ContactValidation
from django.http import HttpResponse
from .forms import ContactForm, ContactFormset, ContactValidationForm
from clients.models import Clients
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.views import View
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa



@login_required(login_url='login')
def creation_contact(request, pk):
    client_contact = get_object_or_404(Clients, pk=pk)
    form_contact = ContactForm()

    if request.method == 'POST':
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            contact = form_contact.save(commit=False)
            contact.client_contact = client_contact
            contact.save()
            return redirect('client_list')

    else:
        form_contact = ContactForm()

    context = {
        'form_contact': form_contact,
        'client_contact': client_contact,
    }

    return render(request, 'includes/infoclientcontact.html', context)


@login_required(login_url='login')
class ClientListView(ListView):
    model = Clients


class ClientCreateView(CreateView):
    model = Clients
    fields = [
        'prenom_clients',
        'nom_clients',
        'telephone_clients'
    ]

    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['contact'] = ContactFormset(self.request.POST)
        else:
            data['contact'] = ContactFormset()
        return data

        
    
    def form_valid(self, form):
        context = self.get_context_data()
        contact = context['contact']
        self.object = form.save()
        if contact.is_valid():
            contact.instance = self.object
            contact.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('client_list')


@login_required(login_url='login')
def validation_contact(request):
    validation = Contact.objects.all()
    confirmer = ContactValidation.objects.all()

    context = {
        'validation' : validation,
        'confirmer': confirmer
    }

    return render(request, 'validation_attente.html', context)

@login_required(login_url='login')
def validation_confirmation(request, pk):
    form_validation = ContactValidationForm()
    contact_validation = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form_validation = ContactValidationForm(request.POST or None)
        if form_validation.is_valid():
            newconfirmation = form_validation.save(commit=False)
            newconfirmation.contact_validation = contact_validation
            newconfirmation.save()
        else:
            form_validation = ContactValidationForm()

    
    

@login_required(login_url='login')
def validation_update(request, pk):
    validation = get_object_or_404(ContactValidation, pk=pk)
    clientup = Clients.objects.all()
    clientva = get_object_or_404(Contact, pk=pk)
    form = ContactValidationForm(request.POST or None, instance=validation)
    if form.is_valid():
        newvalidation = form.save(commit=False)
        newvalidation.validation = validation
        newvalidation.save()
        if clientva.client_contact.adresse_clients is None:
            return redirect('clients_update', pk=clientva.client_contact.pk)
        if clientva.client_contact.adresse_clients is not None:
            return redirect('client_info', pk=clientva.client_contact.pk)
       


    
    context = {
            'validation' : validation,
            'form': form,
            'clientup': clientup,
            'clientva': clientva
        }

    return render(request, 'validation_confirmation.html', context)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewContactPDF(View):
    def get(self, request, pk):
        data = Contact.objects.get(pk=pk)
        data_dict = {
            'data': data
        }
        pdf = render_to_pdf('pdf_infocontact.html', data_dict)
        return HttpResponse(pdf, content_type='application/pdf')

@login_required(login_url='login')
def contact_delete(request, pk):
    contactdel = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contactdel.delete()
        return redirect('home')

    return render(request,'delete/contact_delete.html', {})
