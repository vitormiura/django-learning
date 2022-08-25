from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')

def index(request):
    cursos = {
        '1':'Smart',
        '2':'Manufatura',
        '3':'Mecatrônica',
        '4':'Adm'
    }

    dados = {
        'nome_cursos' : cursos
    }

    return render(request, 'index.html', dados)

def cursos(request):
    return render(request, 'curso.html')