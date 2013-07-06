from django.conf import settings
from django.contrib import admin
from django.conf.urls.defaults import *
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
		url(r'^admin/', include(admin.site.urls)),
		#url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views'),
		url(r'^/?$', 'directorio_medico.directorio.views.index'),
		# url(r'^profesionales/(?P<pro_id>\d+)/$', 'directorio_medico.directorio.views.profesionales'),
		# url(r'^mapa/', 'directorio_medico.directorio.views.mapa'),
		# url(r'^lugar/(?P<lugar_id>\d+)/$', 'directorio_medico.directorio.views.mapa_lugar'),	
)

# if settings.DEBUG:
#     urlpatterns += patterns('django.contrib.staticfiles.views',
#         url(r'^static/(?P<path>.*)$', 'serve'),
#     )

if settings.DEBUG and settings.MEDIA_ROOT:
	urlpatterns += patterns('',
		url(r'%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 
			'django.views.static.serve',
			{'document_root' : settings.MEDIA_ROOT }),)