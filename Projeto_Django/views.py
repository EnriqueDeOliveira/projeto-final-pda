import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    path = os.path.join(settings.BASE_DIR, 'site', 'index.html')
    with open(path, 'r') as arquivo:
        pagina = Template(arquivo.read())
    ctx = Context()
    documento = pagina.render(ctx)
    return HttpResponse(documento)

#chamando arquivo html 'sobre'
def sobre(request):
    path = os.path.join(settings.BASE_DIR, 'site', 'sobre.html')
    with open(path, 'r') as arquivo:
        pagina = Template(arquivo.read())
    ctx = Context()
    documento = pagina.render(ctx)
    return HttpResponse(documento)

#chamando arquivo html 'contato'
def contato(request):
    path = os.path.join(settings.BASE_DIR, 'site', 'contato.html')
    with open(path, 'r') as arquivo:
        pagina = Template(arquivo.read())
    ctx = Context()
    documento = pagina.render(ctx)
    return HttpResponse(documento)

def login(request):
    path = os.path.join(settings.BASE_DIR, 'site', 'login.html')
    with open(path, 'r') as arquivo:
         pagina = Template(arquivo.read())
    ctx = Context()
    documento = pagina.render(ctx)
    return HttpResponse(documento)
       