# To-do-challenge
Challenge API REST Django

## Qué queremos que hagas:

- El Challenge consiste en crear una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.
- La entrega del resultado será en un nuevo fork de este repo y deberás hacer una pequeña demo del funcionamiento y desarrollo del proyecto ante un super comité de las más grandes mentes maestras de Invera, o a un par de devs, lo que sea más fácil de conseguir.
- Podes contactarnos en caso que tengas alguna consulta.

## Objetivos:

El usuario de la aplicación tiene que ser capaz de:

- Crear una tarea
- Eliminar una tarea
- Marcar tareas como completadas
- Poder ver una lista de todas las tareas existentes
- Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma


#### 

La API consta de 4 Endpoints para interactuar

- Creacion de Tarea: Metodo POST "tarea/nueva/" 
	{
    "nombre": "NOMBRE_DE_TAREA",
    "completada": "ESTADO_DE_LA_TAREA" (por defecto FALSE)
	}

- Listar todas las tareas existentes: Metodo GET "tarea/listar/"

- Encontrar/Editar/Eliminar Tarea segun ID: Metodos GET/PUT/DESTROY "tarea/listar/<pk>/"

- Filtrar Tareas segun Fecha de Creacion y/o Nombre: Metodo GET "tarea/filtrar/search="FECHA_CREACION"+"NOMBRE"