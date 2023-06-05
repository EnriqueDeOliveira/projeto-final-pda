from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
   
#chamando arquivo html 'sobre'
def sobre(request):
    return render(request,'sobre.html')
   

#chamando arquivo html 'contato'
def contato(request):
     return render(request,'contato.html')
    

def login(request):
    return render(request,'login.html')
   
def cadastro(request):
    return render(request,'cadastro.html')
    
       
