from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from pycpfcnpj import cpfcnpj
# Create your views here.
cnpj=''
def inicio(request):
    return render(request,'index.html')

def adesao(request):
    if request.method=="POST":
        cnpj=request.POST['CNPJ']
        if cpfcnpj.validate(cnpj)==False:
            messages.info(request, 'O CNPJ é inválido')
            return render(request,'index.html')

        else:
            return render(request,'page.html')
def passa_cnpj():
    return(cnpj)
