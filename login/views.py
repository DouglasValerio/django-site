from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

#def login(request):
    #return render(request,'login.html')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        senha=request.POST["senha"]
 #authenticate(username=user.username, password=raw_password)
        user=auth.authenticate(username=username,password=senha)
        if user is not None:
            auth.login(request,user)
            return redirect('perfil')
        else:
            messages.info(request,"Usuário ou senha inválidos")
            return redirect('login')

    else:
        return render(request,'login.html')
