import os

from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
import pdfkit
from xhtml2pdf import pisa
from django.template import RequestContext

from my_app.models import User
from my_app.forms import UserForm


# def main_page(request):
#     # result = BytesIO()
#     # pdfkit.from_file(template, "example.pdf")
#     # return HttpResponse(result.getvalue(), content_type="application/pdf")


def pdf_file(template, result_content):
    template = get_template(template)
    html = template.render({'users': result_content})
    # print(html)
    path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    options = {
        'zoom': 1.00,
        'page-size': 'A4',
        'encoding': 'utf-8',
        'margin-top': '0cm',
        'margin-bottom': '0cm',
        'margin-left': '0cm',
        'margin-right': '0cm'
    }
    # options = {"enable-local-file-access": None}
    # pdfkit.from_file('test.html', 'example.pdf', configuration=config)
    pdfkit.from_string(str(html), 'out.pdf', configuration=config, options=options)
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf, content_type='application/pdf')
    response["Content-Disposition"] = 'filename="users_file.pdf"'
    # os.remove('out.pdf')
    pdf.close()
    return response


def users_pdf(request):
    users = User.objects.all()
    file = pdf_file('users/users_list.html', users)
    return file


class UserListView(ListView):
    model = User
    form_class = UserForm
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    context_object_name = 'users'
    success_url = reverse_lazy('users_list')


# def html_to_pdf(template_source, context_dict={}):
#     template = get_template(template_source)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type="application/pdf")
#     return None
#
# def users_pdf(request):
#     users = User.objects.all()
#     context = {'users': users}
#     pdf_file = html_to_pdf('users/users_list.html', context)
#     return HttpResponse(pdf_file, content_type="application/pdf")


# def html_to_pdf(request):
#     users = User.objects.all()
#     context = {'users': users}
#     response = HttpResponse(content_type='application/pdf')
#     response["Content-Disposition"] = 'filename="users_file.pdf"'
#     template = get_template("users/users_pdf.html")
#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse("We had some errors <pre>" + html + "</pre>")
#     return response
