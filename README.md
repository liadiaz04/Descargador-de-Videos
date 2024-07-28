# Descargador de Videos

## Descripción

Este proyecto consiste en descargar videos de Youtube en diferentes calidades o solo el audio en formato mp3. Utiliza la biblioteca `pytubefix` para las descargas, `tkinter` para la interfaz gráfica y `pillow` para cargar las imágenes que se muestran en la interfaz.

## Características

*   Permite descargar videos de YouTube en alta calidad (1080p), calidad media (720p) y baja calidad (360p).
*   También tiene la opción para descargar solo el audio en formato mp3.
*   Muestra las tres últimas descargas realizadas con el nombre del video y el formato.
*   Indica el estado de descarga con íconos de carga, éxito y error.

## Estructura del proyecto

*   interface.py
Esta clase define la interfaz gráfica utilizando tkinter. Configura todos los elementos visuales y los eventos asociados a los botones.
*   downloader.py
Contiene la lógica para descargar videos de YouTube usando la biblioteca pytubefix.
*   controller.py
Conecta la interfaz con las funciones de descarga. Maneja las validaciones y actualiza la visualización de las descargas recientes.
*   main.py
Este archivo inicia la aplicación creando una instancia de la clase Controller y ejecutando el bucle principal de la interfaz.

## Instalación

Para ejecutarlo primero es necesario clonar el repositorio y luego instalar las siguientes dependencias:

pip install tkinter
pip install pytubefix
pip install pillow


## Uso
Ejecutar la aplicación:
python main.py

![Screenshot 2024-07-27 205559](https://github.com/user-attachments/assets/a5a1ac85-2a9e-4bab-a979-2a4fefac6cca)

1. Ingresa la URL del video de YouTube que deseas descargar.
2. Selecciona la calidad del video o la opción de solo audio.
3. Observa el estado de la descarga y las últimas descargas realizadas.
