# Aprendiendo Django

Django es un framework de desarrollo web para Python, aqui abarcaremos las bases para crear proyectos usando Django

## Programas necesarios

- Python 3
- pip
- VS code / neovim

## Virtual Env

Los entornos virtuales de python nos permiten tener multiples proyectos con dependencias distintas sin que estas causen conflictos entre si.

En arch: 
 ```
 # Para instalar virtualenv:
 sudo pacman -S python-virtualenv
 ```
 ```
 # Para crear un entorno virtual en el directorio actual: 
 virtualenv venv
 ```


## Instalando Django

 **Con el entorno virtual creado y activado:**
 ```
 pip install django
 ```

## Crar un proyecto con Django

Para crear un nuevo proyecto: 

 ```
 django-admin startproject mysite
 ```

 No usar palabras reservadas como python django o test

 Esto crea un proyecto con un manage.py dentro de una carpeta, para crearlo en la carpeta actual: 

 ```
 django-admin startproject mysite .
 ```

Podemos correr el proyecto con: 

```
python manage.py runserver
```
Esto crea un db.sqlite3 nuevo que es la BD por defecto de Django

El servidor arrancara por defecto en el puerto 8000, para arrancarlo en otro puerto: 

```
python manage.py runserver 3000
```

## Estructura de proyecto

El archivo manage.py sirve para correr comandos administrativos.

db.sqlite3 es la base de datos que se usa con Django normalmente para desarrollo, para producción se debería cambiar la base de datos.

### Dentro de /mysite/

El archivo mas importante es settings.py que tendra distintos parametros que cambiaremos para desarrollar nuestras aplicaciones.

El archivo url.py nos ayuda a manejar las direcciones internas del sitio. 

Tanto asgi.py y wsgi.py no estan implicados en el desarrollo sino en la ejecución en producción para servir el contenido fuera de Django. 

## Aplicaciones en Django

Dentro de un proyecto de Django existen las **Aplicaciones** que son secciones que interactuan entre si para dar funcionalidad completa al proyecto.

Para crear las aplicaciones usamos `startapp`: 


```bash
python manage.py startapp blog
```

Para acoplar estas aplicaciones, lo hacemos desde `/mysite`

### Estructura de una app

El archivo principal es `views.py`, ahi se define que es lo que se envia al cliente para que lo vea en pantalla (html). 

Hay una carpeta `/migrations` que se llenará cuando usemos la base de datos mediante el ORM

El archivo `admin.py` nos permitirá acceder a un panel de administrador para crear datos, usuarios, roles y actualizar contenido. 

El archivo `apps.py` es para configurar la aplicacion, similar al `settings.py`.

`models.py` es para crear clases que se convertirán en tablas de sql mediante el ORM que creará las tablas y las actualizará usando los archivos "migrations".

El archivo `tests.py` es para hacer pruebas de lógica en nuestro sitio.

## Hola mundo en Django

Lo haremos en el archivo `views.py` de `/myapp`

Dentro escribimos la funcion: 
```python
def hello(request):
  return HttpResponse("Hello, Django!")
```

Que devolvera el mensaje que se imprimira en pantalla, usando `urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello)
]
```

## Include Django

Para que las aplicaciones manejen sus propias url en lugar de ponerlas todas en `urls.py` crearemos este archivo pero de forma local dentro de `/myapp`.

Ahí agregamos nuestras url: 

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello)
]
```

Y desde el archivo principal `urls.py` importamos estas url con la función `include`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
```

## Trabajando con bases de datos

### Data Models

Para hacer las migraciones: 
```
python manage.py makemigrations
python manage.py migrate
```
Los modelos son codigo de python que se transforma en tablas de sql.

Cada modelo representa una tabla, y sus atributos son campos de la tabla

### Django shell

Para ejecutar una shell interactiva en nuestro proyecto con Django: 

```
python manage.py shell
```

Dentro podemos interacgtuar con nuestra base de datos de la siguiente manera: 

```
>> p = Project(name="Aplication movil")
```

Eso crea una instancia que se agregará a la tabla Project usando: `p.save()`

Project (o cualquier modelo) tiene atributos y funciones estáticas para poder trabajar con nuestra base de datos: 

```
Project.objects.all()
# Te muestra todos los datos de la tabla Project
```

Tenemos a nuestra disposicion funciones utiles como `get(id=3)` o `filter(name="something")`

Esto devolverá el dato contenido en la tabla correspondiente

## Params


