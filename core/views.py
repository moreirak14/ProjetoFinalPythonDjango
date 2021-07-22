from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm,
)

# Create your views here.

# HOME PAGE #
def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'core/index.html', context)

# PESSOAS #
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

# VEICULOS #
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    forms = VeiculoForm()
    data = {'veiculos': veiculos, 'forms': forms}
    return render(request, 'core/lista_veiculos.html', data)

def veiculos_novos(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_veiculos')

# MOVIMENTOS ROTATIVOS #
def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    forms = MovRotativoForm()
    data = {'mov_rotativos': mov_rotativos, 'forms': forms}
    return render(request, 'core/lista_movrotativos.html', data)

def movrotativos_novos(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movrotativos')

# MENSALISTAS #
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    forms = MensalistaForm()
    data = {'mensalistas': mensalistas, 'forms': forms}
    return render(request, 'core/lista_mensalistas.html', data)

def mensalistas_novos(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_mensalistas')

# MOVIMENTOS MENSAIS #
def lista_movmensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    forms = MovMensalistaForm()
    data = {'mov_mensalistas': mov_mensalistas, 'forms': forms}
    return render(request, 'core/lista_movmensalistas.html', data)

def movmensal_novos(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movmensalistas')