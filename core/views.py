from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo
)

# Create your views here.

def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html', {'mov_rotativos': mov_rotativos})