from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render_to_response




def  index(request):
	suma = 6+2
	suma = 'el valor de la suma es %s ' % (suma)
	return render_to_response('persona.html', {'suma': suma })
	
def listado(request):
	a = [1,5,4,8,10]
	return render_to_response('persona.html', {'valores': a })
	

def hola(request):
	return HttpResponse('holaaaaaaaaaa %s' % nombre )