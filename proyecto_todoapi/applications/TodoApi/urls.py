from django.urls import path
from . import views


app_name = "todo_api"

urlpatterns = [
    path(
        'tarea/nueva/',
        views.CreateTareaAPIView.as_view(),
        name = "nueva-tareas"
    ),
    path(
        'tarea/listar/',
        views.ListarTareaAPIView.as_view(),
        name = "listar-tareas"),
    path(
        'tarea/listar/<pk>/',
        views.RUDTareaAPIView.as_view(),
        name = "tarea-por-PK"
    ),
    path(
        'tarea/filtrar/',
        views.FiltrarTareasAPIView.as_view(),
        name = "filtrar-fecha-palabra_clave"
    ),
]
