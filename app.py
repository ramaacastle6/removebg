from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    try:
        # Recibir la imagen
        file = request.files['image']
        if not file:
            return jsonify({'error': 'No se ha proporcionado ninguna imagen'}), 400

        # Leer la imagen y eliminar el fondo usando rembg (que usa U2Net por detrás)
        input_image = Image.open(file)
        output_image = remove(input_image)

        # Guardar la imagen en un buffer para enviarla como respuesta
        buffer = io.BytesIO()
        output_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Devolver la imagen procesada como respuesta
        return send_file(buffer, mimetype='image/png')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
