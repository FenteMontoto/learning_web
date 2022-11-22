# Generated by Django 4.1.3 on 2022-11-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organizacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "delegacion",
                    models.CharField(max_length=20, verbose_name="Delegación"),
                ),
                ("grupo", models.CharField(max_length=25, verbose_name="Grupo")),
                ("servicio", models.CharField(max_length=20, verbose_name="Servicio")),
            ],
            options={
                "verbose_name": "Organizacion",
                "verbose_name_plural": "Organizaciones",
                "ordering": ["delegacion", "grupo"],
                "unique_together": {("delegacion", "grupo", "servicio")},
            },
        ),
    ]
