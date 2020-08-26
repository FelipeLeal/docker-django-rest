# Docker Django REST

> Dockering django project

> Django/Docker/MySQL

---
## Installation

- Run to start django project

```shell
docker-compose up -d --build django
```
- Run to make migrations for the models project
```shell
docker exec -it django_rest python manage.py makemigrations drugstore
```
- Run to migrate your newly created migrations
```shell
docker exec -it django_rest python manage.py migrate
```
- Run tests
```shell
docker exec -it django_rest python manage.py test
```

---
### Setup
First add your own `.env` file to root project, you can use the .env-example

For testing add GRANT PRIVILEGES to environment user
```
GRANT ALL PRIVILEGES ON test_django_rest.* TO 'admin'@'%';
```
___

# Paso a paso Django Rest

> [Docker desktop](https://www.docker.com/products/docker-desktop)

> [Django](https://www.djangoproject.com/)

> [django_rest_framework](https://www.django-rest-framework.org)

> [django_rest_framework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

> [chile-rut](https://github.com/gmgarciag/chile_rut)

---
## Estructura:
```
static/
www/
.env
.env-example
.gitignore
docker-compose.yml
README.md
```

Personalmente siempre he trabajado con Docker Compose por lo cual la infraestructura se encuentra en el archivo ``docker-compose.yml``. El archivo cuenta con dos servicios; *django* y *mysql* ambos comparten un archivo `.env` con variables de entorno.

### Django 
Es una imagen de python detallada en el archivo Dockerfile, en éste seteamos el directorio donde se encuentra nuestro proyecto y realizamos la instalación de dependencias desde archivo requirements
Contiene dos volúmenes enlazados, uno para copiar el framework y otro para almacenar contenido estático, el cual en este proyecto aún no se utiliza.
La comunicación entre los contenedores es posible por medio de los puertos que se encuentran habilitados tanto para container port como host port. 
Django depende del servicio mysql para ser buildeado

### MySQL
Ha diferencia de Django, el servicio mysql no necesita mayores especificaciones para ser buildeada, por lo que llamamos a su imagen directo en el servicio mysql

---
## Configuración

### Ejecutar en terminal para construir y levantar los contenedores con docker
```shell
docker-compose up -d --build django
```
El log the python mostrará un mensaje de error ya que no encuentra el archivo manage.py, para crearlo es necesario crear un proyecto y posterior la aplicación

Comandos necesarios para levantar proyecto:
```schell
docker exec -it django_rest python manage.py startproject {project-name}
docker exec -it django_rest python manage.py startapp {app-name}
```

### **`settings.py`**

El archivo `/www/django_rest/settings.py` contiene referencias a archivo `.env` desde el cual se definen los valores para conectar a base de datos

**INSTALLED_APPS**: Se definen los módulos necesarios para nuestra aplicación

**DATABASES**: Se define el motor de base datos y los parámetros para su conexión

**REST_FRAMEWORK**
* **TEST_REQUEST_DEFAULT_FORMAT**: Acepta JSON Request por defecto para las pruebas
* **DEFAULT_AUTHENTICATION_CLASSES**: Permite autenticación de usuario anónimo
* **DEFAULT_PERMISSION_CLASSES**: Solo usuarios autentificado puede realizar requests
* **DEFAULT_PARSER_CLASSES**: Acepta JSON Request por defecto

**SIMPLE_JWT**
* Se definen la configuración base para la creación de tokens
* **AUTH_TOKEN_CLASSES**: Se define el método para creación de tokens, en este caso SlidinToken nos permite crear token de manera insegura no solicitando datos de usuario
* **SLIDING_TOKEN_LIFETIME**: Tiempo de expiración de un token

**AUTHENTICATION_BACKENDS**: Permite consultas a base datos por usuario anónimo

### **`validators.py`**

El archivo `/www/drugstore/validators.py` contiene métodos para validar campos de la clase Vaccination
* **validate_rut**: define validaciones para rut gracias a modulo *chile-rut*
* **validate_dose**: define validiones para dose

### **`models.py`**

El archivo `/www/drugstore/models.py` contiene las clases que son utilizadas para mapear nuestro modelo lógico en base de datos por el ORM de Django
* **Vaccination Model Class**: implementa validiones para rut y dose

### **`serializers.py`**

El archivo `/www/drugstore/serializers.py` serializa los campos de modelos para ser presentados por nuestras vistas
* **VaccinationSerializer**
* * **to_representation**: Necesaria para la inserción de la foránea `drug_id` en modelo vaccination

### **`views.py`**

El archivo `/www/drugstore/views.py` contiene las vistas necesarias que se encargan de procesar las solicitudes realizadas por medio del wsgi de Django, estas utilizan módulos de la dependencia *rest_framework* y *rest_framework_simplejwt*
* **DrugList Class**
* **DrugDetail Class**
* **VaccinationList Class**
* **VaccinationDetail Class**
* **ValidationView Class**: Se encarga de crear un usuario anónimo para crear el token de tipo *sliding* y le retorna como un *Response*

### **`urls.py`**

El archivo `/www/django_rest/views.py` define el patrón de rutas que el servicio puede procesar

---
## Despliegue

No cuento con experiencia en despliegue continuo, sé que existen varias herramientas y/o formas para realizar un despliegue como Swarm, por medio de algún repositorio que tenga integración con un servicio en la nube, como Amazon Web Services, Google Cloud Platform, Azure or Digital Ocean.
Por lo que este proyecto de sincroniza vía control de versiones en instancia de EC2


---
## Support
Reach out to me at one of the following places!

- Website at <a href="http://felipeleal.cl" target="_blank">`felipeleal.cl`</a>
- Github at <a href="https://github.com/FelipeLeal/" target="_blank">`@FelipeLeal`</a>

---

## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://felipeleal.cl" target="_blank">felipeleal.cl</a>.
