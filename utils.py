import cv2
import numpy as np

def process_image(file):
    # Lee la imagen usando OpenCV
    file.seek(0)  # Asegúrate de que el puntero del archivo esté al principio
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    
    # Aquí puedes aplicar tu lógica para eliminar el fondo o modificar la imagen
    # (ejemplo: convertir a fondo gris)
    gray_background = np.full(image.shape, 128, dtype=np.uint8)  # Fondo gris
    mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) > 10  # Crea una máscara simple
    result = np.where(mask[:, :, None], image, gray_background)  # Aplica la máscara

    # Guarda la imagen procesada en un archivo temporal
    output_path = 'processed_image.png'
    cv2.imwrite(output_path, result)

    return output_path  # Devuelve la ruta del archivo procesado
