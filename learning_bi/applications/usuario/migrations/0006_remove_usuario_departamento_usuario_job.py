# Generated by Django 4.1.3 on 2022-11-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0005_usuario_delegacion_usuario_departamento_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="usuario", name="departamento",),
        migrations.AddField(
            model_name="usuario",
            name="job",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Función"
            ),
        ),
    ]
