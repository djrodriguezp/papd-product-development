# Docker y Docker Compose

## Archivos del Ejercicio
- Jupyter Notebook con prueba de conexión entre el contenedor de Jupyter y MySQL Server [docker.ipynb](docker.ipynb)
- Definición de Docker Compose: [docker-compose.yml](docker-compose.yml)
- Jupyter Notebook con prueba de conexión entre contenedores creados con Docker Compose [docker-compose.ipynb](docker-compose.ipynb)

## Ejecutando contenedores con Docker

Creamos la red my_test_network con el comando **docker network create**

![Crear red my_test_network](images/image3.png)

Hacemos pull de de imagen de Jupyter Notebook  con el comando **docker pull**

![Pull de imagen de Jupyter Notebook](images/image7.png)

Creamos un contenedor de Jupyter en el puerto TCP 8888 y red my_test_network

![Creación de contenedor de Jupyter Notebook](images/image10.png)

Hacemos pull de de imagen de MySQL versión 5.7.35

![Pull de la imagen de MySQL](images/image5.png)

Creamos el contenedor de MySQL con las respectivas variables de entorno en el puerto TCP 3306 y red my_test_network

![Creación de contenedor de MySQL](images/image11.png)

Probamos la conexión al servidor de MySQL desde el cliente de MySQL

![Conexión exitosa al servidor de MySQL](images/image12.png)

Validamos que ambos contenedores se encuentren corriendo con el comando **docker ps**

![docker ps](images/image8.png)

Instalamos mysql-connector-python en el contenedor de Jupyter

![Instalar mysql-connector-python](images/image2.png)

Se confirma la IP del contenedor de MySQL con el comando **docker inspect my_test_network**

![Validar IP servidor MySQL](images/image4.png)

Probamos la conexión desde el contenedor de Jupyter hacia MySQL

![Se valida conexión entre Jupyter Notebook y Mysql](images/image13.png)

## Docker Compose

Definimos el archivo **docker-compose.yml** para los contenedores de Jupyter Notebooks y MySQL

![Definición de docker-compose.yml](images/image1.png)

Iniciamos los contenedores con el comando **docker-compose up**

![Iniciamos contenedores con docker-compose](images/image9.png)

Validamos la conexión desde el contenedor de Jupyter Notebook hacia MySQL Server

![Se valida conexión entre Jupyter Notebook y Mysql](images/image6.png)
