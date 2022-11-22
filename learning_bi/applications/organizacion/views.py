from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Organizacion

# Create your views here.

class IndexView(TemplateView):
    template_name= 'organizacion/index.html'
    
class Modelo_Lista(ListView):
    model=Organizacion
    template_name="organizacion/listar_organizaciones.html"
    context_object_name='lista_organizaciones'
    