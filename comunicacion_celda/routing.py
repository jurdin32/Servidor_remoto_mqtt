from django.urls import path
from .consumers import datos_recibidos, Iniciar_celda, Detener_celda, Activar_colocacion, Detener_colocacion, Activar_taladrado, Desactivar_taladrado, Reiniciar_celda
ws_urlpatterns=[
    path('ws/datos_recibidos/', datos_recibidos.as_asgi()),
    path('ws/iniciar_celda/', Iniciar_celda.as_asgi()),
    path('ws/detener_celda/', Detener_celda.as_asgi()),
    path('ws/activar_colocacion/', Activar_colocacion.as_asgi()),
    path('ws/detener_colocacion/', Detener_colocacion.as_asgi()),
    path('ws/activar_taladrado/', Activar_taladrado.as_asgi()),
    path('ws/desactivar_taladrado/', Desactivar_taladrado.as_asgi()),
    path('ws/reiniciar_celda/', Reiniciar_celda.as_asgi())
]