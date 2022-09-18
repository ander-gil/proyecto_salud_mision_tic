from django.urls import path
from gestionTransaccion.views import EmpresaView, PersonasView, UsuarioView

urlpatterns = [
    path('Empresas/',EmpresaView.as_view(),name = 'Listar'),
    path('Persona/',PersonasView.as_view(),name = 'Listar'),
    path('Persona/<str:id_persona>',PersonasView.as_view(),name = 'buscar'), 
    path('Usuario/',UsuarioView.as_view(),name = 'Listar')                          
]


