from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
@login_required()
def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'core/index.html', context)

# PESSOAS #
@login_required()
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    forms = PessoaForm()
    data = {'pessoas': pessoas, 'forms': forms}
    return render(request, 'core/lista_pessoas.html', data)

@login_required()
def pessoas_novas(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_pessoas')

@login_required()
def pessoas_update(request, id):
    data = {}
    pessoas = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoas)
    data['pessoas'] = pessoas
    data['forms'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoas_update.html', data)

@login_required()
def pessoas_delete(request, id):
    pessoas = Pessoa.objects.get(id=id)
    if request.method == 'POST':
            pessoas.delete()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoas})

# VEICULOS #
@login_required()
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    forms = VeiculoForm()
    data = {'veiculos': veiculos, 'forms': forms}
    return render(request, 'core/lista_veiculos.html', data)

@login_required()
def veiculos_novos(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_veiculos')

@login_required()
def veiculos_update(request, id):
    data = {}
    veiculos = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculos)
    data['veiculos'] = veiculos
    data['forms'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculos_update.html', data)

@login_required()
def veiculos_delete(request, id):
    veiculos = Veiculo.objects.get(id=id)
    if request.method == 'POST':
            veiculos.delete()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculos})

# MOVIMENTOS ROTATIVOS #
@login_required()
def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    forms = MovRotativoForm()
    data = {'mov_rotativos': mov_rotativos, 'forms': forms}
    return render(request, 'core/lista_movrotativos.html', data)

@login_required()
def movrotativos_novos(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movrotativos')

@login_required()
def movrotativos_update(request, id):
    data = {}
    movrotativos = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativos)
    data['movrotativos'] = movrotativos
    data['forms'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/movrotativos_update.html', data)

@login_required()
def movrotativos_delete(request, id):
    movrotativos = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
            movrotativos.delete()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movrotativos})

# MENSALISTAS #
@login_required()
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    forms = MensalistaForm()
    data = {'mensalistas': mensalistas, 'forms': forms}
    return render(request, 'core/lista_mensalistas.html', data)

@login_required()
def mensalistas_novos(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_mensalistas')

@login_required()
def mensalistas_update(request, id):
    data = {}
    mensalistas = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalistas)
    data['mensalistas'] = mensalistas
    data['forms'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/mensalistas_update.html', data)

@login_required()
def mensalistas_delete(request, id):
    mensalistas = Mensalista.objects.get(id=id)
    if request.method == 'POST':
            mensalistas.delete()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalistas})

# MOVIMENTOS MENSAIS #
@login_required()
def lista_movmensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    forms = MovMensalistaForm()
    data = {'mov_mensalistas': mov_mensalistas, 'forms': forms}
    return render(request, 'core/lista_movmensalistas.html', data)

@login_required()
def movmensal_novos(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movmensalistas')

@login_required()
def movmensal_update(request, id):
    data = {}
    movmensal = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensal)
    data['movmensal'] = movmensal
    data['forms'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/movmensal_update.html', data)

@login_required()
def movmensal_delete(request, id):
    movmensal = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
            movmensal.delete()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movmensal})
