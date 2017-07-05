from django.shortcuts import render

# Create your views here.
from django.views import View

from webapp.forms import PersonaForm
from webapp.models import Persona


class PersonaList(View):
    def get(self, request):
        personas = Persona.objects.all()
        personas_list = []

        if len(personas) > 0:
            personas_list = personas

        context = {'personas_list': personas_list}
        return render(request, 'webapp/home.html', context)


class PersonaCreateView(View):
    def get(self, request):
        persona_form = PersonaForm()

        context = {'form': persona_form}

        return render(request, 'webapp/persona_create.html', context)

    def post(self, request):
        persona_form = PersonaForm(request.POST)

        message = ""

        if persona_form.is_valid():
            persona_form.save()
            persona_form = PersonaForm()
            message = 'Registrado correctamente'

        context = {'form': persona_form, 'message': message}
        return render(request, 'webapp/persona_create.html', context)