from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ESTADO_CIVIL = (
	(0, 'SOLTERO(A)'),
	(1, 'CASADO(A)'),
	(2, 'VIUDO(A)'),
)

SEVERIDAD = (
	(0, 'MODERADO'),
	(1, 'MODERADO A SEVERO'),
	(2, 'SEVERO'),
)

class especialidad(models.Model):
	nombre = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Especialidades"

class ciudad(models.Model):
	ciudad = models.CharField(max_length=50)
	def __unicode__(self):
		return self.ciudad
	class Meta:
		verbose_name_plural = "Ciudades"
	
		
class prevision(models.Model):
	nombre = models.CharField(max_length=50,unique=True)
	def __unicode__(self):
		return self.nombre

class alergias(models.Model):
	nombreAlergia=models.CharField(max_length=40)
	reaccion = models.CharField(max_length=20)
	severidad = models.IntegerField(choices=SEVERIDAD, default=0)

class persona(models.Model):
	user = models.OneToOneField(User,unique=True)
	rut = models.CharField(max_length=15,unique=True)
	nombre = models.CharField(max_length=40)
	apellido_paterno = models.CharField(max_length=30)
	apellido_materno = models.CharField(max_length=30)
	fono = models.PositiveIntegerField(max_length=10)
	celular=models.PositiveIntegerField(max_length=10)
	direccion = models.CharField(max_length=80)
	ciudad = models.ForeignKey(ciudad)
	estadoCivil = models.IntegerField(choices=ESTADO_CIVIL, default=0)
	fechaNacimiento = models.DateField()
	def __unicode__(self):
		return u'%s %s' % (self.rut)
	class Meta:
		abstract = True
		ordering = ['rut', 'nombre' , 'apellido_paterno' , 'apellido_materno']
		verbose_name_plural = "Personas"

class paciente(persona):
	prevision = models.ForeignKey(previsiones)
	alergias = models.ForeignKey(alergias)

		
class medico(persona):
	especialidades = models.ManyToManyField(especialidad)
	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellido_paterno)
	class Meta:
		ordering = ['nombre' , 'apellido_paterno' , 'apellido_materno']
		verbose_name_plural = "Medicos"


