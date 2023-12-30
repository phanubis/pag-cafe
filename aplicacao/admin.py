from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class CadastroCliente(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'codigo', 'usado']
    search_fields = ['nome', 'email', 'telefone']
    list_filter = ['usado']