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

---
### Setup
First add your own `.env` file to root project, you can use the .env-example

For testing add GRANT PRIVILEGES to environment user
```
GRANT ALL PRIVILEGES ON test_django_rest.* TO 'admin'@'%';
```

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
