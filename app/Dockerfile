# Se utiliza de base imagen de python con python 2.7
FROM ubuntu:18.04
ARG DJANGO_ENV

# Agregamos los requerimientos a la imagen
ADD requirements /app/requirements

# update repos
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-add-repository --yes --update ppa:ubuntugis/ppa
RUN apt-get install gdal-bin -y
RUN apt-get install libgdal-dev -y

RUN apt-get update -y && apt-get upgrade -y

# instalar deps
RUN apt-get install -y build-essential libpq-dev \
	python3-dev libffi-dev python3-pip wget \
	pkg-config libpng-dev

RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal

# Asignamos el directorio de trabajo
WORKDIR /app/

# Instalar dependencias de python
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements/$DJANGO_ENV.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
# Crear usuario sin privilegios
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
USER app
