from django.forms import ModelForm
from django import forms 
from holamundo.models import Persona, Alumno, Ramo


class PersonaFormulario(ModelForm):
	class Meta:
		model = Alumno
		#exclude = {'Ramos'}
		
class formularioBuscar(forms.Form):
	q = forms.CharField(required=True)
	ramos = forms.ModelChoiceField(queryset=Alumno.objects.all())
	
