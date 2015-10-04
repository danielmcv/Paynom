from django.db import models

class empleador(models.Model):
	name = models.CharField(max_length=255)

class empleado(models.Model):
	name = models.CharField(max_length=255)
	
		


# Create your models here.
