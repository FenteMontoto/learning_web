from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    CreateView,
)

from .models import Usuario

# Create your views here.


class Lista_Usuarios(ListView):
    template_name='usuario/lista_usuarios.html'
    model=Usuario
    context_object_name='lista'
    
class Lista_Usuarios_Delegacion(ListView):
    template_name='usuario/lista_usuarios_delegacion.html'
   
    def get_queryset(self):
        area=self.kwargs['delegacion']
        lista=Usuario.objects.filter(
        delegacion=area
    )
        return lista
    
    
class UsuarioCreateView(CreateView):
    
    template_name="usuario/add.html"
    model=Usuario
    fields=('__all__')
    success_url=reverse_lazy('usuario_app:correcto')
    