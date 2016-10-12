# Cargar un Imagen con Django 1.10, Django Rest Framework y AngularJS
Esta aplicación del tutorial de Django fue creada con el fin de hacer una demostración de subida de IMAGEN usando Django y Django Rest Framework. Muestra los fundamentos de la escritura de un extremo de Django Rest que permite cargar y recuperar fotos.

## Guía de inicio rápido
###Pasos de instalación si desea probarlo
```
$ git clone https://github.com/dantecrm/ImageUpload-Django-Rest-AngularJS.git
$ cd ImageUpload-Django-Rest-AngularJS
$ virtualenv -p python3.4 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ mkdir uploaded_media
$ cd django_rest_imageupload_backend
$ python manage.py migrate # Migrando tu modelo a la base de datos
$ python manage.py runserver # Iniciando la aplicación
```
