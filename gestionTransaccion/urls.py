from django.urls import path
from gestionTransaccion.views import EmpresaView, PersonasView, UsuarioView, TransaccionesView

urlpatterns = [
    path('Empresas/',EmpresaView.as_view(),name = 'Listar'),
    path('Persona/',PersonasView.as_view(),name = 'Listar'), 
    path('Usuario/',UsuarioView.as_view(),name = 'Listar'),
    path('Transacciones/<str:id_empresa>', TransaccionesView.as_view(), name='buscar'),                       
    path('Transacciones/',TransaccionesView.as_view(),name = 'Listar'),                       
]


