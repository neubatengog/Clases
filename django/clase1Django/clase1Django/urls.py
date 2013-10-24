from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'holamundo.views.listado', name = 'vista_principal'),
    url(r'^listado/$', 'holamundo.views.listado', name = 'vista_listado'),
	url(r'^ingreso/$', 'holamundo.views.ingreso', name= 'vista_ingreso'),
	url(r'^edicion/(?P<alumno_id>\d+)/$', 'holamundo.views.edicion', name= 'vista_edicion'),
	

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
