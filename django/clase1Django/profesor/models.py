from django.db import models
from estudiante.models import Persona, Estudiante, Ramo

# Create your models here.


class Profesor(Persona):
	Ramos = models.ManyToManyField(Ramo)
	
	def __unicode__(self):
		return '%s %s' % (self.nombre , self.apellidos)
	
	class Meta:
		verbose_name_plural="Profesores"