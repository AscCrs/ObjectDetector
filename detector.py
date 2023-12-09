import cv2

# Inicializa la captura de video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Define el clasificador de Rubik
rubikDetector = cv2.CascadeClassifier('functionalTrain/cascade.xml')

while True:
    # Lee un frame de la cámara
    ret, frame = cap.read()

    # Convierte el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta el cubo de Rubik en la imagen en escala de grises
    detections = rubikDetector.detectMultiScale(
        gray,
        scaleFactor=7,  # Ajuste de escala para mejorar la detección
        minNeighbors=100,  # Ajuste de vecinos mínimos para reducir falsos positivos
        minSize=(70, 70),  # Tamaño mínimo del objeto a detectar
    )

    # Dibuja un rectángulo alrededor de cada detección
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
            frame,
            "Cubo detectado",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
            cv2.LINE_AA,
        )

    # Muestra el frame con las detecciones
    cv2.imshow("Deteccion de Objeto", frame)

    # Presionar la tecla 'Esc' para salir
    if cv2.waitKey(1) == ord("q"):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()

