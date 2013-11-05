from django.forms import ModelForm
from django import forms
from estudiante.models import Persona, Estudiante, Ramo

class PersonaForm(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    email = forms.EmailField()

class EstudianteForm(forms.Form):
	nombre = forms.CharField(required=True)
	apellidos = forms.CharField(required=True)
	email = forms.EmailField(required=False)
	matricula = forms.CharField(required=True)
	ramos = forms.ModelMultipleChoiceField(queryset=Ramo.objects.all()) # empty_label=None
	
class EstudianteFormulario(ModelForm):
	class Meta:
		model = Estudiante
		#exclude = {'campo'}
		
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False)) 