from django.db import models

class Empresa(models.Model):
    id_empresa=models.IntegerField(primary_key=True)
    nombre=models.TextField(max_length=45,unique=True,null=False)
    nit=models.TextField(max_length=45,unique=True,null=False)
    ciudad=models.TextField(max_length=45,null=True)
    direccion=models.TextField(max_length=45,null=True)
    telefono=models.TextField(max_length=45,null=True)
    sectorProductivo=models.TextField(max_length=45,null=True)
    estado=models.IntegerField(null=True)
    fechaCreacion=models.DateTimeField(auto_now=True)  
     
    
class Personas(models.Model):
    id_persona=models.IntegerField(primary_key=True)
    nombre=models.TextField(max_length=45,null=True)
    apellidos=models.TextField(max_length=45,null=True)
    email=models.EmailField(unique=True)
    telefono=models.TextField(max_length=45)
    fechaCreacion=models.DateTimeField(auto_now=True)
    
        
class Usuario(models.Model):
    id_usuario=models.IntegerField(primary_key=True)
    email=models.EmailField(unique=True)
    nombre=models.TextField(max_length=45,null=True)
    password=models.TextField(max_length=45,null=True)
    nombre_rol=models.TextField(max_length=45)    
    fechaCreacion=models.DateTimeField(auto_now=True)
    id_persona=models.OneToOneField(Personas, on_delete=models.CASCADE)
    id_empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
           
    
class Transacciones(models.Model):
    id_transaccion=models.IntegerField(auto_created=True,primary_key=True)
    fecha=models.DateField(auto_now=True)
    concepto=models.TextField(max_length=45,null=True)
    monto=models.IntegerField(null=True)
    id_usuario_tran=models.IntegerField(unique=True,null=True)
    tipoTransaccion=models.TextField(max_length=45)
    fechaCreacion=models.DateTimeField(auto_now=True)
    id_empresa=models.IntegerField(null=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
