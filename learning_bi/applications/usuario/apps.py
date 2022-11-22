from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.usuario"
from django.apps import AppConfig


class OrganizacionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "usuario.organizacion"
