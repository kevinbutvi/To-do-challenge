from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import TareaSerializer 
from .models import Tareas
from applications.TodoApi import serializers


# Create your views here.

class CreateTareaAPIView(CreateAPIView):
    """ Api para Creacion de Tareas"""
    
    serializer_class = TareaSerializer


class RUDTareaAPIView(RetrieveUpdateDestroyAPIView):
    """ Api para buscar, actualizar y eliminar tareas """
    
    serializer_class = TareaSerializer
    queryset = Tareas


class ListarTareaAPIView(ListAPIView):
    """ API para listar todas las tareas Lista todas las tareas"""
    
    serializer_class = TareaSerializer
    
    def get_queryset(self):
        """ """
        
        return(Tareas.objects.all())


class FiltrarTareasAPIView(ListAPIView):
    """ API para listar Tareas FILTRADAS por fecha y/o palabras claves en contenido """
    
    queryset = Tareas.objects.all()
    serializer_class = TareaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['created', 'nombre']

