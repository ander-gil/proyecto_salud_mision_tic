from django.urls import path
from gestionTransaccion.views import EmpresaView, PersonasView, UsuarioView, TransaccionesView
from gestionTransaccion.viewLogin import *

urlpatterns = [
    path('Empresas/',EmpresaView.as_view(),name = 'Listar'),
    path('Empresas/<str:id_empresa>', EmpresaView.as_view(), name='buscar'),
    path('Persona/',PersonasView.as_view(),name = 'Listar'),
    path('Persona/<str:id_persona>',PersonasView.as_view(),name = 'buscar'),  
    path('Usuario/',UsuarioView.as_view(),name = 'Listar'),
    path('Transacciones/<str:id_empresa>', TransaccionesView.as_view(), name='buscar'),                       
    path('Transacciones/',TransaccionesView.as_view(),name = 'Listar'),  
    path('ingresar/',iniciarSesion,name='ingresar')                       
]


