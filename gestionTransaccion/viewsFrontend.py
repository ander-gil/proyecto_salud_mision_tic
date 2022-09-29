from cgitb import reset
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

def principal(request):
    return render(request,"administrador.html")

def consultaTransacciones(request):
    response=requests.get('http://localhost:8000/transaccion/Transacciones')
    transacciones=response.json()
    return render(request,"transacciones.html",transacciones)

def formularioTransaccion(request):
    return render(request,"formTransaccion.html")