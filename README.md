# Nuestro Blog de CoderHouse (PROYECTO FINAL)


Este es el **"Blog"** de **Franco Llanos** y **Agustin Mondani**. El mismo fue realizado para el curso de Python de CoderHouse utilizando todas las herramientas dadas por el mismo con la versión de Python **3.10.7** y la versión de Django **4.1.1**.

Todo lo que contiene el Blog

Diario para suscribirse, posteos, artículos, una barra de búsqueda para palabras claves, registro de usuarios, el admin de Django y comentarios en los post.

La forma en que nos desempeñamos al momento de hacer el proyecto fue de forma ordenada, siempre contribuyendo los dos en todos los procesos y etapas del mismo, y con mucha ayuda de internet para poder darle estilo a la página y poder conseguir un resultado amigable y fácil de usar.

*Presentación del Blog:*
---
	https://youtu.be/mYL_oKgvTZ8

Pasos a seguir para poder clonar el repositorio y utilizarlo
===
-Clonar el repositorio
--- 
	git clone https://github.com/AgustinMondani/ProyectoFinalCoder.git

-Correr en la terminar el comando para crear el entorno virtual
---
	python -m venv env

-Para levarlo ejecutar el comando(comando para Windos)
---
	env\Scripts\activate

En Mac o Linux probar con
---
	source env/bin/activate

-Ingresar a la carpeta *app*
---
	cd app

-Instalar todas la dependecias que sean necesarios y que pida
---
	pip install -r requirements.txt --no-cache
	pip freeze
	install environ --- python -m pip install django-environ
	install dj-database-url --- python -m pip install dj-database-url

-Crear archivo .env de variables de entorno
---
	cp .env.example .env

-Crear la *key* con la shell
---
	python manage.py shell
	from django.core.management.utils import get_random_secret_key
	print(get_random_secret_key())

-Copiar la *key* que nos imprime y pegarla en *SECRET_KEY*
---
	\ProyectoFinalCoder\app\.env 

-Dentro de esa ruta y debe quedar *asi*
---
	SECRET_KEY= *AL KEY COPIADA*
	DEBUG=True
	ALLOWED_HOSTS=*,

-Migraciones(crear)
---
	python manage.py makemigrations

-Migraciones(ejecutar)
---
	python manage.py migrate

-Crear el *SuperUsuario*, ingresar nombre, email y password
---
	python manage.py createsuperuser

-Generar statics
---
	python manage.py collectstatic

-Y finalmente correr el servido para poder utilizar el Blog
---
	python manage.py runserver
