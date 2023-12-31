from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save



class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=12, unique=True)
    codigo = models.CharField(max_length=6, unique=True)
    usado = models.BooleanField(default=False)
    concordo_termos = models.BooleanField(default=False)
    promo_email =  models.BooleanField(default=False)
    
def validar_checkboxes(instance, **kwargs):
    if not instance.concordo_termos or not instance.promo_email:
        raise ValueError('Você deve concordar com os termos e condições e aceitar receber promoções por e-mail.')

pre_save.connect(validar_checkboxes, sender=Cliente)
