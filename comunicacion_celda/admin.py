from django.contrib import admin

# Register your models here.

from .models import Datos_celda,Mensajes_celda, Historial_control

admin.site.register(Datos_celda)
admin.site.register(Mensajes_celda)
admin.site.register(Historial_control)

