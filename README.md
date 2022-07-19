# M&D2CKAN
Aplicación encargada de exportar los datos de [M&D Manager](https://github.com/SDMXISTATTOOLKIT/META-DATA.MANAGER) a [CKAN](https://ckan.org/).

![indexa](imagenes/indexa-logo.png)
![ckan](imagenes/logo-ckan.svg)\

## Despliegue

En un entorno con Python instalado, intsalar los requisitos de dependencias.

    pip3 install -r requirements.txt

## Ejecución
Con el directorio de trabajo en la raiz del proyecto ejecutar el fichero main.py

    MDM2CKAN
    └── src
        └── main.py                    # Fichero de ejecución

## Documentación
[MDM2CKAN](https://enprava.readthedocs.io/en/latest/)


# Información para desarrolladores del repositorio
## Ejecutar Integración continua en local

Tox es una herramienta de automatización para python, se puede instalar con pip:
    
    pip install tox
    
Sus comandos son los siguientes:

### Ejecutar Tests, Lint y Compilar la documentación

    tox

### Ejecutar tests

    tox -e py310

### Ejecutar Lint

    tox -e lint

### Compilar la documentación

    tox -e docs

Para compilar la documentación se hace uso del paquete make, se debe instalar en caso de no tenerlo presente en el entorno de trabajo.

## Integración continua
Github está configurado con dos distintas comprobaciones.

### Tox

Se ejecutará cada vez que se haga una Pull request y realizara el comando Tox completo. Indicandote si todo a ido bien.

### Publicación del paquete en Python

Se ejecutará cada vez que se haga una Pull Request a la rama "Main".

Solamente pasará si el paquete no existe previamente en el repositorio de paquetes, por lo tanto cuando estemos seguros de que todo está finalizado deberemos hacer uso de los comandos:

    bumpversion minor 

Dentro de la version actual del paquete, incrementa en 1 la subversion

    bumversion major (Incrementa la version)
    
 Incrementa la version del paquete
