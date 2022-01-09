from django.urls import path
from .views import supervision, login

urlpatterns =[
    path('',supervision),
    path('ola/',login)
]