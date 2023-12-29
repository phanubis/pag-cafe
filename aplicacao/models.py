from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    codigo = models.CharField(max_length=6, unique=True)
    usado = models.BooleanField(default=False)
