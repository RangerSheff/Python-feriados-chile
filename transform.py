import requests
import logging
from datetime import datetime

# Función para obtener feriados desde la API externa
def fetch_feriados(year: int):
    url = f"https://apis.digital.gob.cl/fl/feriados/{year}"
    headers = {
        "User-Agent": "python-http-client",
        "Accept": "application/json",
        "Connection": "keep-alive"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=True, verify=False)
        response.raise_for_status()
        feriados = response.json()
        logging.info(f"Feriados obtenidos: {len(feriados)} para el año {year}")
        return feriados
    except requests.exceptions.RequestException as exc:
        logging.error(f"Error al realizar la solicitud: {exc}")
        return []

# Función para transformar los datos
def transformar_feriados(feriados):
    datos_transformados = []
    for feriado in feriados:
        try:
            fecha = datetime.strptime(feriado["fecha"], "%Y-%m-%d")
            dia_semana = fecha.strftime("%A")
            datos_transformados.append({
                "nombreFeriado": feriado.get("nombre", ""),
                "fecha": feriado["fecha"],
                "tipo": feriado.get("tipo", ""),
                "descripcion": feriado.get("comentarios", ""),
                "dia_semana": dia_semana
            })
        except KeyError as e:
            logging.error(f"Error al transformar datos: clave faltante {e}")
    return datos_transformados
