# Generated by Django 4.0.2 on 2022-06-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_paquete_precio_paquete_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paquete',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
