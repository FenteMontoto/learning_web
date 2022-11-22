from django.contrib import admin
from .models import Usuario, Skill
# Register your models here.

admin.site.register(Skill)


class Usuario_Admin(admin.ModelAdmin):
    list_display=(
        'cod_gestor',
        'delegacion',
        'grupo_titular',
    )
    
admin.site.register(Usuario,Usuario_Admin)
