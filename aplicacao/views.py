from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
import uuid

# Create your views here.

def BASE(request):
    return render(request, 'index.html')


def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        codigo = str(uuid.uuid4())[:6]

        cliente = Cliente.objects.create(
            nome = nome,
            email = email,
            telefone = telefone,
            codigo = codigo
        )
        
        return HttpResponse('Cliente cadastrado com sucesso!')
    return render(request, '.html')