import json
from optparse import Values
from venv import create
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from gestionTransaccion.models import Empresa, Personas, Usuario


class EmpresaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        data = json.loads(request.body)
        empresa = Empresa(id_empresa = data['id_empresa'],nombre = data['nombre'],nit = data['nit'],ciudad = data['ciudad'],direccion = data['direccion'],telefono= data['telefono'],sectorProductivo = data['sectorProductivo'],estado=data['estado'],fechaCreacion=data['fechaCreacion'])
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

class PersonasView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id_usuario = ""):
        if len(id_usuario) > 0:
            Persona = list(Personas.objects.filter(id_usuario = id_usuario).values())
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
        persona=Personas(id_usuario=data['id_usuario'],nombre=data['nombre'],apellidos=data['apellidos'],email=data['email'],telefono=data['telefono'],fechaCreacion=data['fechaCreacion'])
        persona.save()
        datos={'mensaje': 'Persona registrada exitosamente'}
        return JsonResponse(datos)

    def put(self,request,id_usuario):
        data=json.loads(request.body)
        persona=list(Personas.objects.filter(id_usuario=id_usuario).values())
        if len(persona)>0:
            per=Personas.objects.get(id_usuario=id_usuario)
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
    
    '''def get(self,request,id_usuario = ""):
        if len(id_usuario) > 0:
            Usuario = list(Usuario.objects.filter(id_usuario = id_usuario).values())
            if len(Usuario) > 0:
                datos = {"Usuarios": Usuario }
            else:
                datos = {"Mensaje": "No se encontro usuario"} 
        else:
            Usuario = list(Usuario.objects.values())
            if len(Usuario) > 0:
                datos = {"mensaje": Usuario}
            else:
                datos = {"mensaje": "No se encontraron usuarios"}
        return JsonResponse(datos)'''
    
    def post(self,request):
        data=json.loads(request.body)
        print(data)
        try:
            print('entrando al try')
            print(data['personas_id_usuarios_id'])
            per=Personas.objects.get(id_usuario=data['personas_id_usuarios_id'])
            print('primer get')
            print(per)
            print(data['empresas_id_empresa_id'])
            empr=Empresa.objects.get(id_empresa=data['empresas_id_empresa_id'])
            print('segundo get') 
            print(empr)
            print('crear usuario')       
            usu=Usuario.objects.create(id_usuario=data['id_usuario'],email=data['email'],nombre=data['nombre'],password=data['password'],nombre_rol=data['nombre_rol'],fechaCreacion=data['fechaCreacion'],personas_id_usuarios_id=per,empresas_id_empresa_id=empr)
            usu.save()
            mensaje={'Mensaje':'Usuario registrado'}
        except Usuario.DoesNotExist:
            mensaje={"Mensaje":"Usuario no existe"}
        except Exception as e:
            mensaje={"Mensaje":e}
        return JsonResponse(mensaje)
            
  
        