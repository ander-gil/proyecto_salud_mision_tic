# Generated by Django 4.1 on 2022-09-11 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=45, unique=True)),
                ('nit', models.TextField(max_length=45, unique=True)),
                ('ciudad', models.TextField(max_length=45, null=True)),
                ('direccion', models.TextField(max_length=45, null=True)),
                ('telefono', models.TextField(max_length=45, null=True)),
                ('sectorProductivo', models.TextField(max_length=45, null=True)),
                ('estado', models.IntegerField(null=True)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=45, unique=True)),
                ('apellidos', models.TextField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.TextField(max_length=45)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('nombre', models.TextField(max_length=45)),
                ('password', models.TextField(max_length=45, null=True, unique=True)),
                ('nombre_rol', models.TextField(max_length=45)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
                ('empresas_id_empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionTransaccion.empresa')),
                ('personas_id_usuarios_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionTransaccion.personas')),
            ],
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id_transaccion', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('concepto', models.TextField(max_length=45, null=True)),
                ('monto', models.IntegerField(null=True)),
                ('id_usuario', models.IntegerField(null=True, unique=True)),
                ('tipoTransaccion', models.TextField(max_length=45)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
                ('id_empresa', models.IntegerField(null=True)),
                ('usuario_id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionTransaccion.usuario')),
            ],
        ),
    ]