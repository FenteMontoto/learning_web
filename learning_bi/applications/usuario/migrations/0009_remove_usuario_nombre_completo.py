# Generated by Django 4.1.3 on 2022-11-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0008_usuario_nombre_completo"),
    ]

    operations = [
        migrations.RemoveField(model_name="usuario", name="nombre_completo",),
    ]
