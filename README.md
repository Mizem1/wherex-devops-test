# WherEx DevOps Test
![Logo de WherEx](https://wherex.com/wp-content/themes/wherex-mexico/images/logo.svg?x83834)
Prueba tecnica WhereEx para DevOps Jr.

## Requerimientos

- Creación de servicio en Flask (Python) para la obtencion de métricas para CPU y RAM (psutil)
- Creación de dockerfile para la creación de un contenedor con docker
- Creación de un script en shell (Bash) para la automatización del despliegue
- Creación de un pipeline CI/CD en github actions

## Python - Flask & psutil

Se utilizan las siguientes librerias para devolver en formato JSON distintas métricas del sistema
```python
Flask==2.0.1
psutil==5.8.0

#psutils dependencies
Werkzeug==2.0.1
```
El servicio expone un endpoint /metrics que devuelve un JSON con el siguiente formato al realizar una peticion GET
```json
{
    "data":{
        "cpu_usage_percent": FLOAT,
        "memory":{
            "total_gb": FLOAT,
            "used_gb":FLOAT
        }
    },
    "status": TEXT ("success")
}
```



## Docker - Dockerfile

El dockerfile es creado priorizando la rapidez y la minimización del espacio ocupado por el contenedor, utilizando Alpine
```Docker
FROM python:3.11-alpine
```

Con esta imagen y una vez copiado todos los archivos necesarios al contenedor instalamos las dependencias para poder compatibilizar el contenedor Alpine con las dependencias necesarias de python
```Docker
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --no-cache-dir -r requirements.txt
```

Finalmente, se expone el puerto por defecto de Flask (5000) y se corre el comando para ejecutar el aplicativo
```Docker
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
```

## Shell script - Bash

El script de bash deploy.sh permite la automatización del despliegue de la aplicación pasando por 3 pasos principales

1. Verificación, detención y eliminación de contenedores e imagenes anteriores para poder iniciar el servicio
```bash
docker ps -q -f name=$CONTAINER_NAME     [Verifica si existe el contenedor]
docker ps -q --filter "publish=$PORT"    [Verifica si existe un contenedor con el mismo puerto]
docker images -q $IMAGE_NAME:latest      [Verifica si existe una imagen con el mismo nombre]
```

2. Construcción del contenedor en base al Dockerfile
```bash
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .
```
3. Iniciación del contenedor automáticamente al reiniciar el servidor
```bash
echo "Iniciando un nuevo contenedor..."
docker run -d --name $CONTAINER_NAME -p $PORT:5000 --restart unless-stopped $IMAGE_NAME
echo "El contenedor se ha iniciado y se configuró para reiniciarse automáticamente."
```

## CI/CD con Github Actions

Creación de un pipeline con Github Actions en ".github/workflows/main.yml" para la automatización CI/CD. El pipeline sigue los siguientes pasos

- Clonación de código
```
    name: Checkout code
    uses: actions/checkout@v3
```

- Instalación de Python
```
    name: Set up Python
    uses: actions/setup-python@v4
    with:
        python-version: '3.11'
```

- Instalación de dependencias
```
    name: Install dependencies
    run: pip install -r requirements.txt pytest pytest-flask pytest-mock
```

- Pruebas unitarias
```
    name: Run tests
    run: |
        export PYTHONPATH=$(pwd)
        pytest
```


- Ejecución deploy.sh
```
    name: Run deploy script
    run: |
        chmod +x deploy.sh
        ./deploy.sh
```
      

- Período de espera

```
    name: Wait for deployment
    run: sleep 10
```
      

- Verificación de despliegue
```
    name: Verify deployment
    run: curl -f http://localhost:5000/metrics
```


## Como ejecutar el servicio

1. Clonar el repositorio: 
   ```bash
   git clone https://github.com/claudeus123/wherex-devops-test
   ```

2. Entrar al directorio
   ```bash
   cd wherex-devops-test
   ```

3. Dar permisos y ejecutar el script de deploy
    ```bash
   chmod u+x deploy.sh
   ./deploy.sh
   ```

4. Entrar al servicio para obtener las métricas
    ```
    http://localhost:5000/metrics
    ```