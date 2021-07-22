from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)

from .forms import PessoaForm

# Create your views here.

def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    forms = PessoaForm()
    data = {'pessoas': pessoas, 'forms': forms}
    return render(request, 'core/lista_pessoas.html', data)

def pessoas_novas(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html', {'mov_rotativos': mov_rotativos})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})


def lista_movmensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', {'mov_mensalistas': mov_mensalistas})

