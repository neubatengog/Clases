from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=35)
	apellidos = models.CharField(max_length=60)
	def __unicode__(self):
		return u'%s  %s' % (self.nombre , self.apellidos)

	def __str__(self):
		return '%s' % (self.nombre)
	
class Ramo(models.Model):
	nombre = models.CharField(max_length=35)
	def __unicode__(self):
		return self.nombre
			
	

class Alumno(Persona):
	matricula = models.PositiveIntegerField()
	Ramos = models.ManyToManyField(Ramo)
		

		
