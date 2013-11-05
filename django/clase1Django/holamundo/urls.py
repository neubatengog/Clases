from django.conf.urls import patterns, include, url
import settings


# Uncomment the next two lines to enable the admin:
# DESCOMENTAR LAS DOS LINEAS para habilitra el panel administrativo
from django.contrib import admin
admin.autodiscover()

#sistema de autentificacion de django


urlpatterns = patterns('',
	 url(r'^$', 'estudiante.views.index_view', name='vista_indice'),
	
	 url(r'^login/$','estudiante.views.login_usuario',name='vista_login'),
	 url(r'^logout/$','estudiante.views.logout_usuario',name='vista_logout'),
	
	 url(r'^estudiante/', include('estudiante.urls')),
	 url(r'^profesor/', include('profesor.urls')),
	
   	 url(r'^admin/', include(admin.site.urls)),
	 #validar la ruta
	 url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT} ),

)
