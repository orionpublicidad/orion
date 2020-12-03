from django.shortcuts import render
from Orion.models import models_empresa

def listempresa(request):
    data = {
        'title': 'Empresas',
        'empresas': Empresa.objects.all()
    }
    return render(request, 'empresa/list_empresa.html', data)
