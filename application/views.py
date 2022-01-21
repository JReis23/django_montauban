from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import UserForm
from projets.models import Entites, Projets
from clients.models import Clients
from django.core.paginator import Paginator
from django.views import View
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


# def signup(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')

#     else:
#         form = UserForm()


#     context ={
#         'form' : form
#     }

#     return render(request, 'signup.html', context)


@login_required(login_url='login')
def home(request, *args, **kwargs):
    projet = Projets.objects.order_by('-id')
    entite = Entites.objects.all()
    client = Clients.objects.all()
    paginator = Paginator(projet, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'projet': projet,
        'entite': entite,
        'client': client,
        'page_obj': page_obj
    }
    return render(request, 'home.html', context)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    def get(self, request, pk):
        data = Clients.objects.get(pk=pk)
        data_dict = {
            'data': data
        }
        pdf = render_to_pdf('pdf_infoclient.html', data_dict)
        return HttpResponse(pdf, content_type='application/pdf')


# class DownloadPDF(View):
#     def get(self, request, *args, **kwargs):

#         pdf = render_to_pdf('pdf.html', data_dict)

#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "Invoice_%s.pdf" % ("12341231")
#         content = "attachment; filename='%s'" % (filename)
#         response['Content-Disposition'] = content
#         return response
