from xml.dom.xmlbuilder import DOMImplementationLS
from django.shortcuts import render
import json
from django.views import View
from gestionTransaccion.models import Empresa
from django.http import JsonResponse


class EmpresaView(View):
    def post(self,request):
        data = json.loads(request.body)
        empresa = Empresa(id_empresa = data['id_empresa'],nombre = data['nombre'],nit = data['nit'],ciudad = data['ciudad'],direccion = data['direccion'],telefono= data['telefono'],sectorProductivo = data['sectorProductivo'],estado=data['estado'],fechaCreacion=data['fechaCreacion'])
        empresa.save()
        datos = {'mensaje':'Empresa registrada exitosamente !'}
        return JsonResponse(datos) 

    def get(self,request,id_Empresa=""):
        if len(id_Empresa)>0:
            empresa=list(Empresa.objects.filter(id_Empresa=id_Empresa).values())
            if len(empresa)>0:
                datos={"Empresa":Empresa}                
            else:
                datos={'mensaje':"No se encontro Empresa."}
        else:
            Empresa=list(Empresa.objects.values())
            if len(Empresa)>0:
                datos={"mensaje": Empresa}
            else:
                datos={"mensaje":"No se encontraron Empresas."}
        return JsonResponse(datos)

