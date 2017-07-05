from django.forms import ModelForm

from webapp.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        exclude = []
