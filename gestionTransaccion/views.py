import json
from optparse import Values
from venv import create
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from gestionTransaccion.models import Empresa, Personas, Usuario, Transacciones


class EmpresaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        data = json.loads(request.body)
        empresa = Empresa(  id_empresa = data['id_empresa'],
                            nombre = data['nombre'],
                            nit = data['nit'],
                            ciudad = data['ciudad'],
                            direccion = data['direccion'],
                            telefono= data['telefono'],
                            sectorProductivo = data['sectorProductivo'],
                            estado=data['estado'])
        empresa.save()
        datos = {'mensaje':'Empresa registrada exitosamente !'}
        return JsonResponse(datos) 

    def get(self,request,id_empresa = ""):
        if len(id_empresa) > 0:
            Empresas = list(Empresa.objects.filter(id_empresa = id_empresa).values())
            if len(Empresas) > 0:
                datos = {"Empresas": Empresas }
            else:
                datos = {"Mensaje": "No se encontraro empresas"} 
        else:
            Empresas = list(Empresa.objects.values())
            if len(Empresas) > 0:
                datos = {"mensaje": Empresas}
            else:
                datos = {"mensaje": "No se encontraron empresas"}
        return JsonResponse(datos)
    
    def put(self,request,id_empresa):
        data = json.loads(request.body)
        empresa = list(Empresa.objects.filter(id_empresa = id_empresa).values())        
        if len(empresa) > 0:
            emp = Empresa.objects.get(id_empresa = id_empresa)
            emp.nombre = data["nombre"]
            emp.nit = data["nit"]
            emp.ciudad = data["ciudad"]
            emp.direccion = data["direccion"]
            emp.telefono = data["telefono"]
            emp.sectorProductivo = data["sectorProductivo"]
            emp.estado = data["estado"]            
            mensaje = {"mensaje":"Empresa actualizada exitosamente"}
        else:
            mensaje = {"mensaje":"no se encontró empresa"}
        return JsonResponse(mensaje)    

class PersonasView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id_persona = ""):
        if len(id_persona) > 0:
            Persona = list(Personas.objects.filter(id_persona = id_persona).values())
            if len(Persona) > 0:
                datos = {"Personas": Persona }
            else:
                datos = {"Mensaje": "No se encontro persona"} 
        else:
            Persona = list(Personas.objects.values())
            if len(Persona) > 0:
                datos = {"mensaje": Persona}
            else:
                datos = {"mensaje": "No se encontraro persona"}
        return JsonResponse(datos)
    
    def post(self,request):
        data=json.loads(request.body)
        persona=Personas(id_persona=data['id_persona'],
                         nombre=data['nombre'],
                         apellidos=data['apellidos'],
                         email=data['email'],
                         telefono=data['telefono'])
        persona.save()
        datos={'mensaje': 'Persona registrada exitosamente'}
        return JsonResponse(datos)

    def put(self,request,id_persona):
        data=json.loads(request.body)
        persona=list(Personas.objects.filter(id_persona=id_persona).values())
        if len(persona)>0:
            per=Personas.objects.get(id_persona=id_persona)
            per.nombre=data["nombre"]
            per.apellidos=data["apellidos"]
            per.email=data["email"]
            per.telefono=data["telefono"]
            per.save()
            mensaje={"mensaje":"Persona actualizada exitosamente"}
        else:
            mensaje={"mensaje":"No se ha encontrado la persona"}
        return JsonResponse(mensaje)
    
class UsuarioView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        data=json.loads(request.body)
        try:
            per=Personas.objects.get(id_persona=data['id_persona_id'])
            empr=Empresa.objects.get(id_empresa=data['id_empresa_id'])  
            usu=Usuario.objects.create(id_usuario=data['id_usuario'],
                                       email=data['email'],
                                       nombre=data['nombre'],
                                       password=data['password'],
                                       nombre_rol=data['nombre_rol'],
                                       id_persona=per,
                                       id_empresa=empr)
            usu.save()
            mensaje={'Mensaje':'Usuario registrado'}
        except Usuario.DoesNotExist:
            mensaje={"Mensaje":"Usuario no existe"}
        except Exception as e:
            mensaje={"Mensaje":str(e)}
        return JsonResponse(mensaje)
    
    
    def get(self,request,id_usuario = ""):
        if len(id_usuario) > 0:
            usuario = list(Usuario.objects.filter(id_usuario = id_usuario).values())
            if len(usuario) > 0:
                datos = {"Usuario": usuario }
            else:
                datos = {"Mensaje": "No se encontro usuario"} 
        else:
            usuario = list(Usuario.objects.values())
            if len(usuario) > 0:
                datos = {"mensaje": usuario}
            else:
                datos = {"mensaje": "No se encontraro persona"}
        return JsonResponse(datos)
    
class TransaccionesView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        data=json.loads(request.body)
        try:
            usuario=Usuario.objects.get(id_usuario=data['id_usuario_id'])
            empresa=Empresa.objects.get(id_empresa=data['id_empresa_id'])  
            transa=Transacciones.objects.create(id_transaccion=data['id_transaccion'],
                                                concepto=data['concepto'],
                                                monto=data['monto'],
                                                tipoTransaccion=data['tipoTransaccion'],
                                                id_empresa=empresa,
                                                id_usuario=usuario)
            transa.save()
            mensaje={'Mensaje':'Transaccion registrada con exito'}
        except Usuario.DoesNotExist:
            mensaje={"Mensaje":"Usuario no existe"}
        except Exception as e:
            mensaje={"Mensaje":str(e)}
        return JsonResponse(mensaje)
    
    
    def get(self,request,id_empresa=""):
        if len(id_empresa) > 0:
            transaccion = list(Transacciones.objects.filter(id_empresa = id_empresa).values())
            if len(transaccion) > 0:
                datos = {"Transacciones": transaccion }
            else:
                datos = {"Mensaje": "No se encontro Transacciones asociadas a esta empresa"} 
        else:
            transaccion = list(Transacciones.objects.values())
            if len(transaccion) > 0:
                datos = {"mensaje": transaccion}
            else:
                datos = {"mensaje": "No se encontraro Transacciones"}
        return JsonResponse(datos)                    