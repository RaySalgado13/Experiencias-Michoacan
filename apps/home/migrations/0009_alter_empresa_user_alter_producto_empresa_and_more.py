# Generated by Django 4.0.2 on 2022-05-20 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_alter_producto_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='producto',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.empresa'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.tipo_producto'),
        ),
    ]
