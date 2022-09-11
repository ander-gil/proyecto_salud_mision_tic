from django.urls import path
from gestionTransaccion.views import EmpresaView, PersonasView, UsuarioView

urlpatterns = [
    path('Empresas/',EmpresaView.as_view(),name = 'Listar'),
    path('Persona/',PersonasView.as_view(),name = 'Listar'), 
    path('Usuario/',UsuarioView.as_view(),name = 'Usuario')                          
]



