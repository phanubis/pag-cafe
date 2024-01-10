from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Cliente
import uuid

def BASE(request):
    return render(request, 'index.html')

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        codigo = str(uuid.uuid4())[:6]
        concordo_termos = request.POST.get('concordo_termos') == 'on'
        promo_email = request.POST.get('promo_email') == 'on'

        cliente = Cliente.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            codigo=codigo,
            concordo_termos=concordo_termos,
            promo_email=promo_email
        )

        return HttpResponse('Cliente cadastrado com sucesso!')

    return render(request, 'index.html')

def lg(request):
    return render(request, 'lg.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adm')
        else:
            messages.error(request, 'Credenciais inválidas, tente novamente')
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('BASE_URL')



@login_required
def adm(request):
    return render(request, 'adm.html')

