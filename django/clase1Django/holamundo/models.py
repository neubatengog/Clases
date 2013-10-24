from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=35)
	apellidos = models.CharField(max_length=60)
	def __unicode_(self):
		return self.nombre
		
class Ramo(models.Model):
	nombre = models.CharField(max_length=35)
	def __unicode_(self):
		return self.nombre
			
	def __str_(self):
		return '%s' % (self.nombre)	

class Alumno(Persona):
	matricula = models.PositiveIntegerField()
	Ramos = models.ManyToManyField(Ramo)
	def __unicode_(self):
		return self.matricula
		
	def __str_(self):
		return '%s' % (self.nombre)  
		
