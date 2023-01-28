# Kuantaz-ms

### Descripción

Proyecto para la construccion de servicios backend para instituciones, proyectos y usuarios

## Requerimientos

* Python 3.5.2+
* Docker
* Git
* Terminal(Cmder,cmd)

## Diagrama entidad relación

![Diagrama entidad relación](/images/kuantaz-er.png "Diagrama entidad relación")

## Arquitectura de software

Este proyecto fue elaborado bajo ***CLEAN CODE***

## Enfoque de la calidad del código

***Clean as You Code*** haciendo uso de sonarqube para mantener altos estándares de codigo

***Documento de calidad***

![Documento de calidad](/images/kuantaz-sonar.png "Documento de calidad")

## Ejecución con docker

De forma predeterminada, los microservicios se ejecutarán en los siguientes puertos:
- kuantaz-service: 8080

Es necesario tener disponible los puertos mencionados

Pasos:

1. Clone el proyecto.
2. Para ejecutar el servidor en un contenedor Docker, ejecute lo siguiente desde el directorio raíz: **kuantaz-ms**
```bash
# Construir e iniciar el docker
docker-compose up -d --build

# detener el docker
docker-compose down

# Ejecutar pruebas unitarias
docker exec backend-service python -m pytest -rP

# revision de logs generados por el microservicio
  1. docker exec -ti backend-service /bin/bash
  2. cd /usr/src/app/logs
  3. ls
  4. use '''cat''' para ver el log 
```


## Uso

abra su navegador aquí: para ver la definición swagger y ejecutar los endpoints

```
http://localhost:8080/rest/kuantaz-api/v1.0/ui/
```
