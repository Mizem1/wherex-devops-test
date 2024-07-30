#Dockerfile para aplicacion de flask - Alpine y dependencias 
FROM python:3.11-alpine

WORKDIR /usr/src/app

#Copia de archivos necesarios
COPY requirements.txt requirements.txt
COPY app.py .
COPY tests .
COPY utils ./utils

#Instalacion de dependencias
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

