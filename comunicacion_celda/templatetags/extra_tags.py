from django import template
     
register = template.Library()
     
@ register.filter (name = 'cut') # El nombre del filtro cuando se usa en la plantilla
def myCut (valor): # Reemplace el parámetro pasado arg con '~'
    return valor[8]
