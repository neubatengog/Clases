from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render_to_response

from holamundo.forms import PersonaFormulario

#esto es para el token de verificacion contexto
from django.template import RequestContext
from holamundo.models import Persona 

def  index(request):
	suma = 6+2
	suma = 'el valor de la suma es %s ' % (suma)
	return render_to_response('persona.html', {'suma': suma })
	
def listado(request):
	personas = Persona.objects.all()
	return render_to_response('listado.html', {'personas': personas })

def ingreso(request):
	formulario = PersonaFormulario()
	todo_ok = False
	if request.method == 'POST':
		formRecibido = PersonaFormulario(request.POST)
		if formRecibido.is_valid():
			todo_ok= True
			formRecibido.save()			
	return render_to_response('persona.html', {'formulario': formulario, 'todo_ok':todo_ok  }, context_instance=RequestContext(request)) 
	

def hola(request):
	return HttpResponse('holaaaaaaaaaa %s' % nombre )