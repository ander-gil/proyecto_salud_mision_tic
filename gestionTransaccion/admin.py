from django.contrib import admin

# Register your models here.
from gestionTransaccion.models import Empresa
from gestionTransaccion.models import Personas
from gestionTransaccion.models import Usuario
from gestionTransaccion.models import Transacciones


admin.site.register(Empresa)
admin.site.register(Personas)
admin.site.register(Usuario)
admin.site.register(Transacciones)