# Generated by Django 4.1.3 on 2022-11-23 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0010_usuario_nombre_completo"),
    ]

    operations = [
        migrations.RemoveField(model_name="usuario", name="nombre_completo",),
    ]
