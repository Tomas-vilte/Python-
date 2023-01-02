from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import personaForm
from personas.models import persona


# Create your views here.


def detallePersona(request, id):
    # personas = persona.objects.get(pk=id)
    personas = get_object_or_404(persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': personas})


# PersonaForm = modelform_factory(persona, exclude=[])
def editarPersona(request, id):
    if request.method == 'POST':
        formaPersona = personaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = personaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def nuevaPersona(request, id):
    personas1 = get_object_or_404(persona, pk=id)
    if request.method == 'POST':
        formaPersona = personaForm(request.POST, instance=personas1)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = personaForm(instance=personas1)
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request, id):
    personas1 = get_object_or_404(persona, pk=id)
    if personas1:
        personas1.delete()
    return redirect('inicio')
