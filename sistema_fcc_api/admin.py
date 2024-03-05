from django.contrib import admin
from sistema_fcc_api.models import *

admin.site.register(Administradores)
admin.site.register(Alumnos)
admin.site.register(Maestros)

#En este archivo se van a agregar perfiles a registrar