from estudiante.models import Persona, Estudiante, Ramo

from django.contrib import admin

class RamoAdmin(admin.ModelAdmin):
	lista = ('nombre')

admin.site.register(Persona)
admin.site.register(Estudiante)
admin.site.register(Ramo,RamoAdmin)



