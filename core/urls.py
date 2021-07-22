"""estacionamento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoas_novas,
)

urlpatterns = [
    path('', home, name='core.home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novas/', pessoas_novas, name='core_pessoas_novas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mov-mensal/', lista_movmensalistas, name='core_lista_movmensalistas'),

]
