from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=60)
	email = models.EmailField(blank=True , null=True, verbose_name='correo electronico')
	def __unicode_(self):
		return self.nombre
	
	def _get_NombreCompleto(self):
		return u'%s %s' % (self.nombre, self.apellidos)
		
	nombreCompleto = property(_get_NombreCompleto)

class Ramo(models.Model):
	nombre = models.CharField(max_length=40)
	
	def __str__(self):
		return self.nombre
		
	def __unicode_(self):
		return '%s' % (self.nombre)	

class Estudiante(Persona):
	Matricula = models.PositiveIntegerField()
	Ramos = models.ManyToManyField(Ramo)
	
	def __unicode_(self):
		return self.Matricula

	# def __str__(self):
	# 		return u'%s %s' % (self.nombre, self.apellidos) 


	