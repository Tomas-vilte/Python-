from django.forms import ModelForm, EmailInput, TextInput

from personas.models import persona, domicilio


class personaForm(ModelForm):
    class Meta:
        model = persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }


class domicilioForm(ModelForm):
    class Meta:
        model = domicilio
        fields = '__all__'
        widgets = {
            'no_calle': TextInput(attrs={'type': 'number'})
        }
