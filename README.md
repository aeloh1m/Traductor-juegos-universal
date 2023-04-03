# Traductor de juegos universal
Este es un proyecto de traducción de juegos en Python que utiliza la biblioteca de reconocimiento óptico de caracteres Tesseract y la biblioteca wxPython para crear una ventana en la que se puede hacer clic para tomar capturas de pantalla de la ventana activa y traducir los textos utilizando Tesseract OCR.
## Tabla de Contenidos
* [Requisitos](#requisitos)
* [Instalación](#instalacion)
* [Uso](#uso)

## Requisitos:
Primero habrá que tener instalados los siguientes:

- Python y su respectivo PATH en las variables del sistema,

- Pip: Primero dirigirse hasta el directorio " ./dir/to/python/Scripts "
```diff
#Paso 1
En el cmd de windows (o una consola) ejecutar:
> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#Paso 2
> python get-pip.py
```


- Tesseract-OCR (enlace directo): https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe 
también con su respectivo PATH agregado.

Una vez instalado Tesseract-OCR, es necesario también agregar una variable
del sistema nueva:

```diff
- Nombre de la variable: TESSDATA_PREFIX
- Valor de la variable: C:\Program Files\Tesseract-OCR\tessdata
```  

Dentro del directorio "tessdata" previo, en donde se haya instalado, agregar
los [dos archivos](https://github.com/aeloh1m/Traductor-juegos-universal/tree/main/tessdata) dentro de la carpeta "tessdata" en el repositorio .

```diff
Nota: Para agregar algún PATH, primero es necesario tener la dirección donde este
instalado el programa o archivo e ir hasta:
Panel de Control > Sistema > (del lado derecho) Opciones avanzadas del sistema >
Variables de entorno, en la variable path clickear editar y agregar desde "Nuevo",
la dirección del archivo/programa.
```
 
## Instalación:

> py -3.9 -m venv venv

> .\venv\Scripts\Activate.ps1

> pip install unidic-lite Pillow pytesseract cutlet translators wxPython


Una vez teniendo todo listo, ejecutar el script mediante:

> python .\main.py


## Uso
Para utilizar este traductor de juegos, simplemente ejecuta el archivo main.py y sigue las instrucciones en pantalla. La ventana de captura de pantalla se abrirá automáticamente, y puedes hacer clic en cualquier lugar de la ventana para tomar una captura de pantalla de la zona correspondiente. La imagen capturada se procesará automáticamente mediante Tesseract OCR y se mostrará en la ventana de salida.

Ten en cuenta que la calidad de las traducciones depende en gran medida de la calidad de las capturas de pantalla y de la precisión del reconocimiento óptico de caracteres. Por lo tanto, es posible que tengas que ajustar la posición y el tamaño de la ventana de captura de pantalla para obtener los mejores resultados.

## Contribución
Si deseas contribuir a este proyecto, eres bienvenido a hacerlo. Puedes enviar solicitudes de extracción (pull requests) o crear un problema (issue) para informar de algún problema o sugerir alguna mejora.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
