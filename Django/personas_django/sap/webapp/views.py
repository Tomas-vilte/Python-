from django.http import HttpResponse
from django.shortcuts import render

from personas.models import persona


# Create your views here.

def bienvenido(request):
    no_Personas = persona.objects.count()
    personas = persona.objects.all()
    return render(request, 'bienvenido.html', {'no_Personas': no_Personas, 'personas': personas})

