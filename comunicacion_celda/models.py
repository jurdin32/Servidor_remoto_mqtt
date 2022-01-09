from django.db import models

# Create your models here.

class Datos_celda(models.Model):
    cilindros=models.IntegerField()
    Tipo_cilindro=models.CharField(max_length=9)
    Tipo_metal=models.CharField(max_length=9)

class Mensajes_celda(models.Model):
    notificaciones_clasificacion=models.CharField(max_length=70)
    notificaciones_colocacion=models.CharField(max_length=70)

class Historial_control(models.Model):
    A_D_celda=models.BooleanField()
    A_D_colocacion=models.BooleanField()
    A_D_taladrado=models.BooleanField()



# codigo para insertar, borrar, consultar, y editar registros de tablas

#from comunicacion_celda.models import Datos_celda

#datos=Datos_celda(cilindros="1",Tipo_cilindro="plastico",Tipo_metal="") #genera la instruccion sql del tipo insert into
#datos.save()  # se ejecuta la instruccion sql generada

#datos1=Datos_celda.objects.create(cilindros="1",Tipo_cilindro="metal",Tipo_metal="acero") # otra forma de ejecutar el insert en un solo paso

#datos1.Tipo_cilindro="plastico" # ejecutar instruciones del tipo update
#datos1.save()

#datos_eliminar=Datos_celda.objects.get(id=1)   # generar una instruccion del tipo delete
#datos_eliminar.delete()

#consulta_datos=[]
#consulta_datos=Datos_celda.objects.all() # me da una lista de todos los elementos de la tabla es decir es un selec all




