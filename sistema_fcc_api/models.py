from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class Administradores(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_admin = models.CharField(max_length=255, null=False, blank=True)
    telefono = models.CharField(max_length=255, null=False, blank=True)
    rfc = models.CharField(max_length=255, null=False, blank=True)
    edad = models.IntegerField(null=False, blank=True)
    ocupacion = models.CharField(max_length=255, null=False, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del admin "+self.first_name+" "+self.last_name

class Alumnos(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    matricula = models.CharField(max_length=255, null=False, blank=True)
    fecha_nacimiento = models.DateField(auto_now_add=False, null=False, blank=True)
    curp = models.CharField(max_length=255, null=False, blank=True)
    rfc = models.CharField(max_length=255, null=False, blank=True)
    edad = models.IntegerField(null=False, blank=True)
    telefono = models.CharField(max_length=255, null=False, blank=True)
    ocupacion = models.CharField(max_length=255, null=False, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del alumno "+self.first_name+" "+self.last_name 
    
class Maestros(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    id_trabajador = models.CharField(max_length=255, null=False, blank=True)
    fecha_nacimiento = models.DateField(auto_now_add=False, null=False, blank=True)
    telefono = models.CharField(max_length=255, null=False, blank=True)
    rfc = models.CharField(max_length=255, null=False, blank=True)
    cubiculo = models.CharField(max_length=255, null=False, blank=True)
    area_investigacion = models.CharField(max_length=255, null=False, blank=True)
    materias_json = models.TextField(null=False, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del maestro "+self.first_name+" "+self.last_name

#En este archivo se definen las tablas