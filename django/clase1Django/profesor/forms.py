from django.forms import ModelForm
from django import forms
from estudiante.models import Ramo
from profesor.models import Profesor


class ProfesorForm(forms.Form):
	nombre = forms.CharField(required=True)
	apellidos = forms.CharField(required=True)
	email = forms.EmailField(required=False)
	ramos = forms.ModelMultipleChoiceField(queryset=Ramo.objects.all()) # empty_label=None
