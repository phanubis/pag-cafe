from django.shortcuts import render, redirect
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
