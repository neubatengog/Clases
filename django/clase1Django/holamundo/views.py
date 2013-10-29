from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render_to_response

from holamundo.forms import PersonaFormulario, formularioBuscar, FormularioPerso, FormularioLogin

#esto es para el token de verificacion contexto
from django.template import RequestContext

from holamundo.models import Alumno

#redireccionamineto
from django.http import HttpResponseRedirect

#para autentificacion 
from django.contrib.auth import login, logout, authenticate

#decoradores para login
from django.contrib.auth.decorators import login_required

from clase1Django.settings import URL_LOGIN

@login_required(login_url= URL_LOGIN)
def listado(request):
	alumnos = Alumno.objects.all().order_by('apellidos')
	return render_to_response('listado.html', {'alumnos': alumnos }, context_instance=RequestContext(request))

def buscar(request):
	abuscar = request.GET['q']
	alumnos = Alumno.objects.filter(nombre__contains=abuscar).order_by('apellidos')
	return render_to_response('listado.html', {'alumnos': alumnos })
	
@login_required(login_url= URL_LOGIN)	
def edicion(request, alumno_id):
	todo_ok = False
	try:
		alumnos = Alumno.objects.get(pk=alumno_id)
	except Alumno.DoesNotExist:
		alumnos = None
	if request.method == 'POST' and alumnos is not None:
		formRecibido = PersonaFormulario(request.POST, instance=alumnos)
		if formRecibido.is_valid():
			alumnos.save(commit=false)
			
			alumnos.save_m2m()
			
		
			return HttpResponseRedirect('/listado/')
	else:
		formulario = PersonaFormulario(instance=alumnos) 
		return render_to_response('ingreso.html', {'formulario': formulario, 'todo_ok':todo_ok  }, context_instance=RequestContext(request)) 

def eliminar(request, alumno_id):
	todo_ok = False
	try:
		alumnos = Alumno.objects.get(pk=alumno_id)
	except Alumno.DoesNotExist:
		alumnos = None
	if alumnos is not None:
			alumnos.delete()
	return HttpResponseRedirect('/listado/')
	
def prueba(request):
	formuPerso = FormularioPerso()
	return render_to_response('prueba.html', {'formulario': formuPerso}, context_instance=RequestContext(request))

@login_required(login_url= URL_LOGIN)		
def ingreso(request):
	formulario = PersonaFormulario()
	todo_ok = False
	if request.method == 'POST':
		formRecibido = PersonaFormulario(request.POST)
		if formRecibido.is_valid():
			todo_ok= True
			formRecibido.save()			
	return render_to_response('ingreso.html', {'formulario': formulario, 'todo_ok':todo_ok  }, context_instance=RequestContext(request)) 


def login_usuario(request):
	if request.user.is_authenticated():
			##redireccionar a pagina
		return HttpResponseRedirect('/listado/')
	else:
		if request.method == 'POST':
			form = FormularioLogin(request.POST)
			if form.is_valid():
				usuario = form.cleaned_data['username']
				passw = form.cleaned_data['password']
				usuario = authenticate (username = usuario, password = passw)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/listado/')	
	form = FormularioLogin()
	return render_to_response('login.html', {'formulario': form }, context_instance=RequestContext(request))

def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect('/')

