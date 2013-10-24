from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render_to_response

from holamundo.forms import PersonaFormulario

#esto es para el token de verificacion contexto
from django.template import RequestContext
from holamundo.models import Alumno 

#redireccionamineto
from django.http import HttpResponseRedirect

def listado(request):
	alumnos = Alumno.objects.all()
	return render_to_response('listado.html', {'alumnos': alumnos })
	
def edicion(request, alumno_id):
	todo_ok = False
	try:
		alumnos = Alumno.objects.get(pk=alumno_id)
	except Alumno.DoesNotExist:
		alumnos = None
	if request.method == 'POST' and alumnos is not None:
		formRecibido = PersonaFormulario(request.POST, instance=alumnos)
		if formRecibido.is_valid():
			alumnos.save()
			return HttpResponseRedirect('/listado/')
	else:
		formulario = PersonaFormulario(instance=alumnos) 
		return render_to_response('persona.html', {'formulario': formulario, 'todo_ok':todo_ok  }, context_instance=RequestContext(request)) 
	
def ingreso(request):
	formulario = PersonaFormulario()
	todo_ok = False
	if request.method == 'POST':
		formRecibido = PersonaFormulario(request.POST)
		if formRecibido.is_valid():
			todo_ok= True
			formRecibido.save()			
	return render_to_response('persona.html', {'formulario': formulario, 'todo_ok':todo_ok  }, context_instance=RequestContext(request)) 
