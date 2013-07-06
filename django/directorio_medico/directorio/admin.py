from django.contrib import admin
from directorio_medico.directorio.models import *

#admin.site.register(especialidad)
admin.site.register(ciudad)
admin.site.register(prevision)

class MedicoEspecialidad(admin.ModelAdmin):
	list_filters = ('nombre' ,'apellido_paterno', 'apellido_materno')
	search_fields = ('apellido_paterno', 'apellido_materno', 'nombre')
	#filter_horizontal = ('especialidades','atenciones','AtiendePor')
	

	
#admin.site.register(medico,MedicoEspecialidad)
#admin.site.register(atencion)