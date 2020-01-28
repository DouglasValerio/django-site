from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from inicio.views import passa_cnpj
from django.utils import timezone

now = timezone.now()
# Create your views here.

def registro(request):
    if request.method=="POST":
        cnpj=passa_cnpj()
        print(cnpj)
        first_name=request.POST['nome']
        last_name=request.POST['last_name']
        userID=request.POST['user']
        email=request.POST['e-mail']
        senha1=request.POST['senha1']
        senha2=request.POST['senha2']
        #status_registro=request.POST['aceitarRegulamento']
        if senha1==senha2:
            if User.objects.filter(username=userID).exists():
                messages.info(request, 'Usuário já cadastrado')
                return redirect('registro')
            #elif status_registro==2:
                #    messages.info(request, 'Você precisa aceitar os termos e condições.')
                #    return redirect('registro')

            else:
                cnpj=passa_cnpj()
                print(cnpj)
                user=User.objects.create_user(username=userID,password=senha1,first_name=cnpj,last_name=last_name,email=email)
                user.save()
                return redirect('login')
                print('Usuário criado')

        else:
            messages.info(request, 'As senhas não são idênticas')
            return redirect('registro')
    else:
        return render(request,'page.html')
def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def troca_senha(request):
    return render(request, 'troca_senha.html')



def new_password(request):
    userID2=request.POST['usuario_1']
    senha3=request.POST['senha3']
    senha4=request.POST['senha4']
    if senha3==senha4:
        u = User.objects.get(username__exact=userID2)
        u.set_password(senha3)
        u.save()
        return redirect('login')
    else:
        messages.info(request, 'As senhas não são idênticas')
        return redirect('troca_senha')
        #auth.logout(request)
    return render(request, 'troca_senha.html')
