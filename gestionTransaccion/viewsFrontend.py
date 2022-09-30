from cgitb import reset
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

def principal(request):
    return render(request,"administrador.html")

def consultaTransacciones(request):
    response=requests.get('http://localhost:8000/transaccion/Transacciones/1')
    transacciones=response.json()
    return render(request,"transacciones.html",transacciones)

def formularioTransaccion(request):
    return render(request,"formTransaccion.html")

def guardartransaccion(request):        
    datos = {    
        "id_transaccion": request.POST['id_transaccion'],         
        "concepto": request.POST['concepto'],
        "monto": request.POST['monto'],
        "tipoTransaccion":request.POST['tipo_transaccion'],
        "id_empresa_id":request.POST['id_empresa'],
        "id_usuario_id":request.POST['id_Usuario']        
    }
    print(datos)
    requests.post('http://localhost:8000/transaccion/Transacciones/',data = json.dumps(datos))
    return redirect('../consultaTransacciones')