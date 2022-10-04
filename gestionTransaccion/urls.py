from django.urls import path
from gestionTransaccion.views import EmpresaView, PersonasView, UsuarioView, TransaccionesView
from gestionTransaccion.viewLogin import *
from gestionTransaccion.viewsFrontend import *

urlpatterns = [
    path('Empresas/',EmpresaView.as_view(),name = 'Listar'),
    path('Empresas/<str:id_empresa>', EmpresaView.as_view(), name='buscar'),
    path('Persona/',PersonasView.as_view(),name = 'Listar'),
    path('Persona/<str:id_persona>',PersonasView.as_view(),name = 'buscar'),  
    path('Usuario/',UsuarioView.as_view(),name = 'Listar'),
    path('Transacciones/<str:id_empresa>', TransaccionesView.as_view(), name='buscar'),                       
    path('Transacciones/',TransaccionesView.as_view(),name = 'Listar'),  
    path('ingresar/',iniciarSesion,name='ingresar'),
    path('consultaTransacciones/',consultaTransacciones,name='consultar'),
    path('consultaTransaccionesEmp/',ConsultaTransaccionesEmp,name='consultarEmp'),
    path('formTransaccion/',formularioTransaccion,name='formTransaccion'),                       
    path('guardarTransaccion/',guardartransaccion,name='registrar'),
    path('formEmpresa/',formularioEmpresa,name='formEmpresa'),
    path('consultaEmpresas/',consultaEmpresas,name='consultar'),
    path('guardarEmpresa/',guardarEmpresa,name='guardarEmp'),
    path('cargarFormEmpresa/<str:id_empresa>',cargarFormEmpresa,name='cargarFormEmpresa'),
    path('consultaPersonas/',consultaPersonas,name='consultar'),
    path('guardarPersona/',guardarPersona,name='registrar'),
    path('cargarFormPersona/<str:id_persona>',cargarFormPersona,name='formularioPersona'),
    path('formPersona/',formularioPersonas,name='formPersona'),
    path('consultaUsuarios/',consultaUsuarios,name='consultar'),
    path('guardarUsuario/',guardarUsuario,name='registrar'),
    path('formUsuario/',formularioUsuarios,name='formUsuario'),
    path('formAdministrador/',formularioAdministrador,name='formAdministrador'),
    path('formEmpleados/',formularioEmpleados,name='formEmpleados')
    
]