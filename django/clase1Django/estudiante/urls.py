from django.conf.urls import patterns, include, url

urlpatterns = patterns('estudiante.views',
	url(r'^ingreso/$', 'ingreso_estudiante', name='ingreso_estudiante'),
 	url(r'^listado/$', 'listar_estudiante', name='listar_estudiante' ),
	url(r'^editar/(?P<estudiante_id>\d+)/$', 'editar_estudiante', name='editar_estudiante' ),
	url(r'^borrar/(?P<estudiante_id>\d+)/$', 'borrar_estudiante', name='borrar_estudiante' ),
	url(r'^buscar/$', 'buscar_estudiante', name='buscar_estudiante' ),
)