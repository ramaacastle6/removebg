import firebase_admin
from firebase_admin import credentials, storage

# Inicializa Firebase
cred = credentials.Certificate('config/iclothes-6da92-firebase-adminsdk-2pvfy-0adaf4161e.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'iclothes-6da92.appspot.com'
})

def upload_image_to_storage(file):
    bucket = storage.bucket()
    blob = bucket.blob(file.filename)  # Crea un blob con el nombre del archivo
    blob.upload_from_file(file)  # Sube el archivo
    return blob.public_url  # Retorna la URL pública de la imagen
