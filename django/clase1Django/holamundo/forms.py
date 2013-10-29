from django.forms import ModelForm
from django import forms 
from holamundo.models import Persona, Alumno, Ramo


class PersonaFormulario(ModelForm):
	class Meta:
		model = Alumno
		#exclude = {'Ramos'}
class FormularioPerso(PersonaFormulario):
	ramos = forms.ModelChoiceField(queryset=Ramo.objects.all())
	
class FormularioLogin(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class formularioBuscar(forms.Form):
	q = forms.CharField(required=True)
	ramos = forms.ModelChoiceField(queryset=Ramo.objects.all())
	