from django.urls import path
from . import views
from .views import cadastrar, lg, login_view, logout_view, adm

urlpatterns = [
    path('', views.BASE, name='BASE_URL'),
    path('cad', cadastrar, name='cad'),
    path('lg', lg, name='lg'),
    path('login/', login_view, name='login'),
    path('adm/', adm, name='adm'),
    path('logout/', logout_view, name='logout'),

]

