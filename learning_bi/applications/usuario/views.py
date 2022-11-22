from django.shortcuts import render
from django.views.generic import(
    ListView,
)
from .models import Usuario

# Create your views here.


class Lista_Usuarios(ListView):
    template_name='usuario/lista_usuarios.html'
    model=Usuario
    context_object_name='lista'