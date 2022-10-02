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

def ConsultaTransaccionesEmp(request):    
    dato = request.POST.get('id_empresa',False)
    response = requests.get('http://localhost:8000/transaccion/Transacciones/')
    transaccion = response.json()
    return render(request,'transacciones.html',transaccion)
    
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

def formularioEmpresa(request):
    return render(request,"formEmpresa.html")

def consultaEmpresas(request):
    response=requests.get('http://localhost:8000/transaccion/Empresas')    
    empresa=response.json()
    return render(request,"empresas.html",empresa)

def guardarEmpresa(request):        
    datos = {    
        "id_empresa": request.POST['id_empresa'],         
        "nombre": request.POST['nombre'],
        "nit": request.POST['nit'],
        "ciudad":request.POST['ciudad'],
        "direccion":request.POST['direccion'],
        "telefono":request.POST['telefono'],
        "sectorProductivo":request.POST['sectorProductivo'],
        "estado":request.POST['estado']        
    }
    print(datos)
    requests.post('http://localhost:8000/transaccion/Empresas/',data = json.dumps(datos))
    return redirect('../consultaEmpresas')

def cargarFormEmpresa(request,id_empresa):
    response = requests.get('http://localhost:8000/transaccion/Empresas/' + id_empresa)
    empresa = response.json()       
    return render(request,"actualizarEmpresa.html",empresa)
    
    
def formularioPersonas(request):
    return render(request,"formPersona.html")

def consultaPersonas(request):
    response=requests.get('http://localhost:8000/transaccion/Persona')    
    persona=response.json()
    return render(request,"personas.html",persona)

def guardarPersona(request):        
    datos = {    
        "id_persona": request.POST['id_persona'],         
        "nombre": request.POST['nombre'],
        "apellidos": request.POST['apellidos'],
        "email":request.POST['email'],
        "telefono":request.POST['telefono'],      
    }    
    requests.post('http://localhost:8000/transaccion/Persona/',data = json.dumps(datos))
    return redirect('../consultaPersonas')

def cargarFormPersona(request,id_persona):
    response = requests.get('http://localhost:8000/transaccion/Persona/' + id_persona) 
    pesona = response.json()    
    return render(request,"actualizaPersona.html",pesona)



def ActualizarPersona(request):
    codigo = request.POST['id_persona']
    datos={
        "nombre":request.POST['nombre'],
        "apellidos":request.POST['apellidos'],
        "email":request.POST['email'],
        "telefono":request.POST['telefono']        
    }
    requests.put('http://localhost:8000/transaccion/Persona/' + codigo,data=json.dumps(datos))
    return redirect('../consultaPersonas/')

def formularioUsuarios(request):
    return render(request,"formUsuario.html")

def consultaUsuarios(request):
    response=requests.get('http://localhost:8000/transaccion/Usuario')    
    usuario=response.json()
    return render(request,"usuarios.html",usuario)

def guardarUsuario(request):        
    datos = {    
        "id_usuario": request.POST['id_usuario'], 
        "email":request.POST['email'],        
        "nombre": request.POST['nombre'],
        "password": request.POST['password'],        
        "nombre_rol":request.POST['nombre_rol'], 
        "id_persona_id":request.POST['id_persona_id'], 
        "id_empresa_id":request.POST['id_empresa_id']    
    }
    print(datos)
    requests.post('http://localhost:8000/transaccion/Usuario/',data = json.dumps(datos))
    return redirect('../consultaUsuarios')

def formularioAdministrador(request):
    return render(request,"formAdministrador.html")

def formularioEmpleados(request):
    return render(request,"formEmpleados.html")