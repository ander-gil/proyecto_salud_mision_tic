from django.urls import path
from gestionTransaccion.views import EmpresaView, PersonasView, UsuarioView

urlpatterns = [
    path('Empresas/',EmpresaView.as_view(),name = 'Listar'),
    path('Empresas/<str:id_empresa>',EmpresaView.as_view(),name = 'crear'),
    path('Persona/',PersonasView.as_view(),name = 'Listar'), 
    path('Persona/<str:id_usuario>',PersonasView.as_view(),name = 'crear'),
    path('Usuario/',UsuarioView.as_view(),name = 'Usuario')                          
]


