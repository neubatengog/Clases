from django.conf.urls import patterns, include, url

urlpatterns = patterns('profesor.views',
	url(r'^ingreso/$', 'ingreso_profesor', name='ingreso_profesor'),
 	url(r'^listado/$', 'listar_profesor', name='listar_profesor' ),
	url(r'^editar/(?P<profesor_id>\d+)/$', 'editar_profesor', name='editar_profesor' ),
	url(r'^borrar/(?P<profesor_id>\d+)/$', 'borrar_profesor', name='borrar_profesor' ),
	url(r'^buscar/$', 'buscar_profesor', name='buscar_profesor' ),
)