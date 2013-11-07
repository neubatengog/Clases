# Create your views here.
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render_to_response

from profesor.models import Profesor
#Desde forms importamos la clase PersonasForm
from profesor.forms import ProfesorFormulario



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
def ingreso_profesor(request):
	todo_ok = False
	titulo = "Ingresar profesor"
	if request.method == 'POST':
		formulario = ProfesorFormulario(request.POST )
		if formulario.is_valid():
			todo_ok = True
			profesor=formulario.save(commit=False)
			profesor.save()	
			formulario.save_m2m()
			return HttpResponseRedirect(reverse('listar_profesor'))
	else:
		formulario =ProfesorFormulario()
	valores = {'formulario': formulario, 'todo_ok':todo_ok, 'titulo':titulo }
	return render_to_response('ingreso.html' ,valores ,context_instance = RequestContext(request))

@login_required(login_url=URL_LOGIN)
def editar_profesor(request, profesor_id):
	todo_ok = False
	titulo = "Editar Profesor"
	try:
		profesor = Profesor.objects.get(pk=profesor_id)
	except Profesor.DoesNotExist: #excepcion si el profesor no existe
		profesor = None
	if request.method == 'POST' and profesor is not None:
		formulario = ProfesorFormulario(request.POST, instance=profesor)
		if formulario.is_valid():
			todo_ok = True
			profesor=formulario.save(commit=False)
			profesor.save()	
			formulario.save_m2m()
	else:
		formulario = ProfesorFormulario(instance=profesor)
	valores = {'formulario': formulario, 'todo_ok':todo_ok, 'titulo':titulo}
	return render_to_response('ingreso.html' ,valores ,context_instance = RequestContext(request))

#Listar todas los profesores

@login_required(login_url=URL_LOGIN)
def listar_profesor(request):
	titulo = "profesor"
	try:
		profesores = Profesor.objects.all()
	except Profesor.DoesNotExist:
		profesores = None
	return render_to_response('listado.html', {'profesores':profesores , 'titulo':titulo}, context_instance = RequestContext(request))

def borrar_profesor(request, profesor_id):
	Mensaje = "Borrar profesor"
	try:
		profesor = Profesor.objects.get(id=profesor_id)
	except Profesor.DoesNotExist:
		profesor = None
	if profesor is not None:
		Mensaje = "profesor borrado"
		profesor.delete()
	else:
		Mensaje = "profesor no encontrado"
	return HttpResponseRedirect(reverse ('listar_profesor'))


def buscar_profesor(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		profesores = Profesor.objects.filter(Q(nombre__icontains=q) | Q(apellidos__icontains=q))
	else:
		profesores = None
	return render_to_response('listado.html', {'profesores':profesores}, context_instance = RequestContext(request) )



