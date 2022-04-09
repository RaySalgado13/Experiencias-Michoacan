# Generated by Django 3.2.11 on 2022-04-09 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100)),
                ('numero_exterior', models.CharField(max_length=10)),
                ('numero_interior', models.CharField(blank=True, max_length=10)),
                ('colonia', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_legal', models.CharField(max_length=100)),
                ('nombre_comercial', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('rfc', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=10)),
                ('representante', models.CharField(max_length=200)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('fecha_inicio', models.DateTimeField(blank=True)),
                ('fecha_fin', models.DateTimeField(blank=True)),
                ('stock', models.IntegerField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Reporte',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('folio', models.CharField(max_length=250)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=250)),
                ('telefono', models.CharField(blank=True, max_length=10)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
                ('producto', models.ManyToManyField(to='home.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=250)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('monto_total', models.IntegerField()),
                ('items', models.JSONField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipo_reporte')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipo_producto'),
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('enlace', models.TextField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.producto')),
            ],
        ),
    ]
