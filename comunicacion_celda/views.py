# modulo para renderizar la plantilla
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


# Create your views here.



def login(request):
    return render(request,'login.html')


def supervision(request):
    return render(request,'base.html',{'text':'Hola Alex'})
#    return render(request,'index.html',context={'text':'Hola Alex'})

