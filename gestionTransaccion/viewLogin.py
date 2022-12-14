from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from gestionTransaccion.models import Personas, Usuario
from django.contrib import messages

def iniciarSesion(request):
    if request.method =="POST":
        form = AuthenticationForm(request,data = request.POST)        
        if form.is_valid():            
            nombre = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre,password = contraseña)
            if usuario is not None:                
                try:
                    empleado = Usuario.objects.get(email = usuario.email)                                         
                    login(request,usuario)                                        
                    return redirect('../formEmpleados')
                except Usuario.DoesNotExist:
                    if usuario.is_superuser:
                        login(request,usuario)
                        return redirect('../formAdministrador')
                    else:
                        messages.success(request,f'Acceso Denegado') 
            else:
                messages.success(request,f'Usuario no existe')
        else:
            messages.success(request,f'Datos incorrectos') 
    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})                               