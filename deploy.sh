#!/bin/bash

# Definicion de constantes
IMAGE_NAME="wherex-flask-metrics"
CONTAINER_NAME="wherex-flask-metrics-container"
PORT="5000"

echo "Ejecutando script de deploy..."

# Verificacion de la ejecucion de un contenedor anterior - Detencion
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Deteniendo el contenedor $CONTAINER_NAME..."
    docker stop $CONTAINER_NAME
fi

# Verificacion de la existencia de un contenedor que usa el puerto especificado - Detencion
container_using_port=$(docker ps -q --filter "publish=$PORT")
if [ -n "$container_using_port" ]; then
    echo "Deteniendo el contenedor que está usando el puerto $PORT..."
    docker stop $container_using_port
fi

# Verificacion de la ejecucion de un contenedor anterior - Eliminacion
if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then

    echo "Eliminando el contenedor $CONTAINER_NAME..."
    docker rm $CONTAINER_NAME
fi

# Verificacion de la existencia de una imagen anterior - Eliminacion
if [ "$(docker images -q $IMAGE_NAME:latest)" ]; then
    echo "Eliminando la imagen Docker anterior $IMAGE_NAME..."
    docker image rm $IMAGE_NAME:latest
else
    echo "No se encontró una imagen anterior de $IMAGE_NAME para eliminar."
fi

# Construccion de imagen docker en base al Dockerfile
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

# Iniciacion del contenedor con --restart unless-stopped para que se inicie automaticamente al reiniciar el servidor
echo "Iniciando un nuevo contenedor..."
docker run -d --name $CONTAINER_NAME -p $PORT:5000 --restart unless-stopped $IMAGE_NAME
echo "El contenedor se ha iniciado y se configuró para reiniciarse automáticamente."