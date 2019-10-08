from django.db import models
from .models import *
from django.contrib import admin 

# Create your models here.

class Param(models.Model):
	tipo = models.CharField(max_length=5, blank=False)
	codigo = models.CharField(max_length=5, blank=True)
	descrip = models.CharField(max_length=79, null=True)
	valor1 =  models.IntegerField(blank=True)
	valor2 =  models.IntegerField(blank=True)
	valor3 =  models.IntegerField(blank=True)
	sw_1   =  models.IntegerField(blank=True)
	sw_2   =  models.IntegerField(blank=True)
	notas  =  models.TextField(blank=True)
	fecha  =  models.DateTimeField(blank=True)
	corr   =  models.IntegerField(blank=True)
	fecha2 =  models.DateTimeField(blank=True)
	
	def __str__(self):
		return self.codigo.strip() 
