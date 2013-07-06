from django.http import HttpResponse,  HttpResponseRedirect
from django.shortcuts import render_to_response
from models import *


from django import forms
from django.template import RequestContext, Template, Context
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.mail import send_mail

def index(request):
	#especialidades = especialidad.objects.order_by('nombre')
	return render_to_response('tabla.html',context_instance=RequestContext(request))

# def profesionales(request, pro_id):
# 	esp = especialidad.objects.get(id=pro_id)
# 	profesionales = medico.objects.filter(especialidades=pro_id)
# 	profesionales = profesionales.order_by('apellido_paterno','apellido_materno','nombre')
# 	return render_to_response('index.html', {'profesionales':profesionales , 'especialidad': esp} )



	
	