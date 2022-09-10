from django.urls import path
from gestionTransaccion.views import EmpresaView

urlpatterns = [
    path('Empresas/',EmpresaView.as_view(),name = 'Listar')                              
]



