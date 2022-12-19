from django.db import models

# Create your models here.

class Cosechadora (models.Model):
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    plataforma=models.IntegerField()
    anio=models.IntegerField()


class Tractor (models.Model):
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    hp=models.IntegerField()
    anio=models.IntegerField()


class Apero (models.Model):
    tipo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    anio=models.IntegerField()
