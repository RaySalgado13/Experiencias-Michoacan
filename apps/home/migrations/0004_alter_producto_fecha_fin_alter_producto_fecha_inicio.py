# Generated by Django 4.0.2 on 2022-04-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_imagen_producto_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
