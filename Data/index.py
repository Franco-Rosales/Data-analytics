import boto3
from config.config import *

def descargar_desde_s3(key_id, secret_key, bucket_name, archivo_s3, ruta_local):
    # Conexión a S3
    s3 = boto3.client('s3', aws_access_key_id=key_id, aws_secret_access_key=secret_key)

    # Descargar archivo desde S3
    try:
        s3.download_file(bucket_name, archivo_s3, ruta_local)
        print(f"Archivo descargado: {ruta_local}")
    except Exception as e:
        print(f"Error al descargar archivo desde S3: {e}")

# Configuración
key_id = KEY_ID
secret_key = SECRET_KEY
bucket_name = BUCKET_NAME
archivo_disney = "disney_plus_titles.csv"
archivo_netflix = "netflix_titles.csv"

# Descargar archivos
#descargar_desde_s3(key_id, secret_key, bucket_name, archivo_disney, "CSV/disney_plus_titles.csv")
descargar_desde_s3(key_id, secret_key, bucket_name, archivo_netflix, "CSV/netflix_titles.csv")
