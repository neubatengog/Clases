from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render_to_response

from estudiante.models import Persona, Estudiante, Ramo
#Desde forms importamos la clase PersonasForm
from estudiante.forms import EstudianteFormulario, LoginForm



from django.http import HttpResponse
#agregado para csrf token en formulario
from django.template import RequestContext

#redireccionador
from django.http import HttpResponseRedirect
#para redireccionar en base al nombre de la url
from django.core.urlresolvers import reverse

#Operadore OR q
from django.db.models import Q 


#importamos de settings una constante
from Holamundo.settings import URL_LOGIN

#autentificacion
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import authenticate,  login, logout


#decorador para login_required
from django.contrib.auth.decorators import login_required

def index_view(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def ingreso_estudiante(request):
	todo_ok = False
	if request.method == 'POST':
		formulario = EstudianteFormulario(request.POST )
		if formulario.is_valid():
			todo_ok = True
			estudiante=formulario.save(commit=False)
			estudiante.save()	
			formulario.save_m2m()
			return HttpResponseRedirect(reverse ('vista_listar'))
	else:
		formulario = EstudianteFormulario()
		valores = {'formulario': formulario, 'todo_ok':todo_ok}
		return render_to_response('ingreso.html' ,valores ,context_instance = RequestContext(request))

@login_required(login_url=URL_LOGIN)
def editar_estudiante(request, estudiante_id):
	todo_ok = False
	try:
		estudiante = Estudiante.objects.get(pk=estudiante_id)
	except Estudiante.DoesNotExist: #excepcion si el estudinate no existe
		
		estudiante = None
	if request.method == 'POST' and estudiante is not None:
		formulario = EstudianteFormulario(request.POST, instance=estudiante)
		if formulario.is_valid():
			todo_ok = True
			estudiante=formulario.save(commit=False)
			estudiante.save()	
			formulario.save_m2m()
	else:
		formulario = EstudianteFormulario(instance=estudiante)
	valores = {'formulario': formulario, 'todo_ok':todo_ok}
	return render_to_response('ingreso.html' ,valores ,context_instance = RequestContext(request))

#Listar todas los estudiantes

@login_required(login_url=URL_LOGIN)
def listar_estudiante(request):
	try:
		estudiantes = Estudiante.objects.all()
	except Estudiante.DoesNotExist:
		estudiantes = None
	return render_to_response('listado.html', {'estudiantes':estudiantes}, context_instance = RequestContext(request))

def borrar_estudiante(request, estudiante_id):
	Mensaje = "Borrar estudiante"
	try:
		estudiante = Estudiante.objects.get(id=estudiante_id)
	except Estudiante.DoesNotExist:
		estudiante = None
	if estudiante is not None:
		Mensaje = "Estudiante borrado"
		estudiante.delete()
	else:
		Mensaje = "estudiante no encontrado"
	return HttpResponseRedirect('/listado/')


def buscar_estudiante(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		estudiantes = Estudiante.objects.filter(Q(nombre__icontains=q) | Q(apellidos__icontains=q))
	else:
		estudiantes = None
	return render_to_response('listado.html', {'estudiantes':estudiantes}, context_instance = RequestContext(request) )
	
	
def login_usuario(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				next = request.POST['next']
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect(next)
				else:
					mensaje = "usuario y/o password incorrecto"
		next = request.REQUEST.get('next')
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje,'next':next}
		return render_to_response('login.html',ctx,context_instance=RequestContext(request))

def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect('/')
	

	