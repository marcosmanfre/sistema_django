from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno


def home(request):
    return render(request, 'home.html')    

def sigup(request):
  
    if request.method == 'GET':

           return render(request,'sigup.html', {
            'form' : UserCreationForm
        } )   
    
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()

                login(request, user)
                return redirect('cadastro')
            except:

                return render(request, 'sigup.html', {
                'form': UserCreationForm,
                "error": 'Usuário já existe'                           
                })
            
        return render(request, 'sigup.html', {
            'form': UserCreationForm,
            "error" : 'Senhas são diferentes'
        })
    

def sigin(request):

    if request.method == 'GET':
        return render(request, 'sigin.html', {
        'form': AuthenticationForm

        })    
    else:
        user = authenticate (
            request, username =request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'sigin.html', {
                'form': AuthenticationForm,
                'error': 'Usuário ou senha incorreto',
                })
        else:
            login (request, user)
            return redirect('cadastro')
        
@login_required
def sair(request):
    logout (request)
    return redirect('home')   

@login_required
def cadastro(request):
     return render(request, 'cadastro.html', {
        'alunos': Aluno.objects.all()
     })    

