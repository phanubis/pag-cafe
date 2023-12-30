from django.urls import path
from . import views
from .views import cadastrar

urlpatterns = [
    path('', views.BASE, name='BASE_URL'),
    path('cad', cadastrar, name='cad'),
]

