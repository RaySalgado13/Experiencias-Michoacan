# Generated by Django 4.0.2 on 2022-05-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_producto_fecha_fin_alter_producto_fecha_inicio'),
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
