from django.forms import ModelForm
from django import forms 
from holamundo.models import Persona, Alumno


class PersonaFormulario(ModelForm):
	class Meta:
		model = Alumno
		#exclude = {'Ramos'}
		
