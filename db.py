import sqlite3
import logging
from fastapi import HTTPException
from models import Feriado

# Función para almacenar los datos en la base de datos
def almacenar_feriados(datos):
    try:
        conn = sqlite3.connect("feriados.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feriados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombreFeriado TEXT,
                fecha TEXT,
                tipo TEXT,
                descripcion TEXT,
                dia_semana TEXT
            )
        """)

        for feriado in datos:
            cursor.execute("""
                INSERT INTO feriados (nombreFeriado, fecha, tipo, descripcion, dia_semana)
                VALUES (?, ?, ?, ?, ?)
            """, (
                feriado["nombreFeriado"],
                feriado["fecha"],
                feriado["tipo"],
                feriado["descripcion"],
                feriado["dia_semana"]
            ))

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error al interactuar con la base de datos: {e}")
    finally:
        conn.close()

# Función para crear la base de datos y la tabla
def crear_base_datos():
    try:
        conn = sqlite3.connect("feriados.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feriados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombreFeriado TEXT,
                fecha TEXT,
                tipo TEXT,
                descripcion TEXT,
                dia_semana TEXT
            )
        """)

        logging.info("Base de datos y tabla 'feriados' creadas exitosamente.")
    except sqlite3.Error as e:
        logging.error(f"Error al crear la base de datos: {e}")
    finally:
        conn.close()

# Función para obtener un feriado de la base de datos
def obtener_feriado(fecha: str):
    try:
        conn = sqlite3.connect("feriados.db")
        cursor = conn.cursor()

        cursor.execute("SELECT nombreFeriado, fecha, tipo, descripcion, dia_semana FROM feriados WHERE fecha = ?", (fecha,))
        resultado = cursor.fetchone()

        if resultado:
            # Asignamos "" si no hay valor para descripcion
            descripcion = resultado[3] if resultado[3] else ""
            return Feriado(
                nombreFeriado=resultado[0],
                fecha=resultado[1],
                tipo=resultado[2],
                descripcion=descripcion,
                dia_semana=resultado[4]
            )
        else:
            raise HTTPException(status_code=404, detail="Feriado no encontrado")
    except sqlite3.Error as e:
        logging.error(f"Error al consultar la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    finally:
        conn.close()
