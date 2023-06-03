#Importando a biblioteca httpresponse
from django.http import HttpResponse
#import datetime
#importação para manipulação de arquivo externo
from django.template import Template,Context
#importação para manipulação de arquivos xml
#import xml.etree.cElementTree as ET

#chamando arquivo html
def index(request):
   documentoExterno = open("C:/Users/Admin/Desktop/DJANGO/Projeto_Django/site/index.html")
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)

#chamando arquivo html 'sobre'
def sobre(request):
   documentoExterno = open("C:/Users/Admin/Desktop/DJANGO/Projeto_Django/site/sobre.html")
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)

#chamando arquivo html 'contato'
def contato(request):
   documentoExterno = open("C:/Users/Admin/Desktop/DJANGO/Projeto_Django/site/contato.html")                          
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)

         
       