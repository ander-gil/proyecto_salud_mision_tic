import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from gestionTransaccion.models import Empresa

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
            