from fastapi import FastAPI, HTTPException
import logging
from datetime import datetime
from db import crear_base_datos, almacenar_feriados, obtener_feriado
from transform import transformar_feriados, fetch_feriados
from models import Feriado

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuración de FastAPI
app = FastAPI()

# Endpoint para consultar feriados
@app.get("/feriado/{fecha}", response_model=Feriado)
def consultar_feriado(fecha: str):
    try:
        return obtener_feriado(fecha)
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    # Crear la base de datos y tabla si no existen
    crear_base_datos()

    # Ejecución inicial para poblar la base de datos
    year = 2024
    feriados = fetch_feriados(year)
    if feriados:
        datos_transformados = transformar_feriados(feriados)
        almacenar_feriados(datos_transformados)
    else:
        logging.warning("No se pudieron obtener datos de feriados.")
