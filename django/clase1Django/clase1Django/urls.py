from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'holamundo.views.prueba', name = 'vista_principal'),
	 url(r'^login/$', 'holamundo.views.login_usuario', name = 'vista_login'),
	 url(r'^logout/$', 'holamundo.views.logout_usuario', name = 'vista_logout'),
    url(r'^listado/$', 'holamundo.views.listado', name = 'vista_listado'),
	url(r'^ingreso/$', 'holamundo.views.ingreso', name= 'vista_ingreso'),
	url(r'^edicion/(?P<alumno_id>\d+)/$', 'holamundo.views.edicion', name= 'vista_edicion'),
	url(r'^buscar/$', 'holamundo.views.buscar', name= 'vista_buscar'),
	url(r'^eliminar/(?P<alumno_id>\d+)/$', 'holamundo.views.eliminar', name= 'vista_eliminar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
