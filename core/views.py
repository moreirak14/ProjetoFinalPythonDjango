from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {'mensagem': 'Olá Mundo'}
    return render(request, 'core/index.html', context)
