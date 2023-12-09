# Rubik Detector

Detección de objetos usando el algoritmo Haar Cascade para detectar un cubo Rubik a través de una webcam

### Información General
- Tiempo de entrenamiento: Aproximadamente entre 4 - 5 horas
- Objetos positivos utilizados para el entrenamiento: Entre 400 - 1000 aproximadamente
- Objetos negativos utilizados para el entrenamiento: Etre 500 - 900 aproximadamente
- Tamaño de imagén utilizado para el entrenamiento: 38x46 px

### Recursos utilizados
- OpenCV
- Python 3
- imutils
- Cascade Trainer GUI

### Ejemplo de objeto detectado
![alt text][seed]

[seed]: https://github.com/AscCrs/ObjectDetector/blob/main/ImagesTestings/Captura%20de%20pantalla%202023-12-08%20211020.png "Imagen Positiva"

### Ejemplo con otro objeto similar
![alt text][seed]

[seed]: https://github.com/AscCrs/ObjectDetector/blob/main/ImagesTestings/Captura%20de%20pantalla%202023-12-08%20211214.png "Imagen Negativa"

### Ejemplo de objeto detectado con objeto de interferencia
![alt text][seed]

[seed]: https://github.com/AscCrs/ObjectDetector/blob/main/ImagesTestings/Captura%20de%20pantalla%202023-12-08%20211259.png "Imagen Positiva"

### Consideraciones
El número de imgenes utilizadas para el entrenamiento es considerablemente pequeño a comparación de lo necesario para poder obtener un 100% de precisión. El brillo y fondo del cuarto puede causar falsos positivos al tratar de detectar la figura, además de poder existir cierto error de detección por el tamaño utilizado en la configuración del script al tamaño real del objeto (ya que un menor tamaño, hacía imposible la detección).
