# Traductor de juegos universal
Este es un proyecto de traducción de juegos en Python que utiliza la biblioteca de reconocimiento óptico de caracteres Tesseract y la biblioteca PyAutoGUI para crear una ventana en la que se puede hacer clic para tomar capturas de pantalla de la ventana activa y traducir los textos utilizando Tesseract OCR.

## Instalación
Antes de ejecutar el programa, debes instalar las bibliotecas necesarias. Puedes hacerlo ejecutando el siguiente comando:


pip install -r requirements.txt
Este comando instalará todas las bibliotecas necesarias, incluyendo Tesseract, PyAutoGUI y otras.

## Uso
Para utilizar este traductor de juegos, simplemente ejecuta el archivo main.py y sigue las instrucciones en pantalla. La ventana de captura de pantalla se abrirá automáticamente, y puedes hacer clic en cualquier lugar de la ventana para tomar una captura de pantalla de la zona correspondiente. La imagen capturada se procesará automáticamente mediante Tesseract OCR y se mostrará en la ventana de salida.

Ten en cuenta que la calidad de las traducciones depende en gran medida de la calidad de las capturas de pantalla y de la precisión del reconocimiento óptico de caracteres. Por lo tanto, es posible que tengas que ajustar la posición y el tamaño de la ventana de captura de pantalla para obtener los mejores resultados.

## Contribución
Si deseas contribuir a este proyecto, eres bienvenido a hacerlo. Puedes enviar solicitudes de extracción (pull requests) o crear un problema (issue) para informar de algún problema o sugerir alguna mejora.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
