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
    veiculos_novos,
    movrotativos_novos,
    mensalistas_novos,
    movmensal_novos,
    pessoas_update,
    veiculos_update,
    movrotativos_update,
    mensalistas_update,
    movmensal_update,
    pessoas_delete,
    veiculos_delete,
    movrotativos_delete,
    mensalistas_delete,
    movmensal_delete,
)

urlpatterns = [
    path('', home, name='core.home'),

    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novas/', pessoas_novas, name='core_pessoas_novas'),
    path('pessoas-update/<id>', pessoas_update, name='core_pessoas_update'),
    path('pessoas-delete/<id>', pessoas_delete, name='core_pessoas_delete'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novos/', veiculos_novos, name='core_veiculos_novos'),
    path('veiculos-update/<id>', veiculos_update, name='core_veiculos_update'),
    path('veiculos-delete/<id>', veiculos_delete, name='core_veiculos_delete'),

    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novos/', movrotativos_novos, name='core_movrotativos_novos'),
    path('mov-rot-update/<id>', movrotativos_update, name='core_movrotativos_update'),
    path('mov-rot-delete/<id>', movrotativos_delete, name='core_movrotativos_delete'),

    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalistas-novos/', mensalistas_novos, name='core_mensalistas_novos'),
    path('mensalistas-update/<id>', mensalistas_update, name='core_mensalistas_update'),
    path('mensalistas-delete/<id>', mensalistas_delete, name='core_mensalistas_delete'),

    path('mov-mensal/', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('mov-mensal-novos/', movmensal_novos, name='core_movmensal_novos'),
    path('mov-mensal-update/<id>', movmensal_update, name='core_movmensal_update'),
    path('mov-mensal-delete/<id>', movmensal_delete, name='core_movmensal_delete'),
]
