# Proyecto de Feriados - API REST

Este es un proyecto de Python que utiliza FastAPI para exponer una API REST que consulta y gestiona información sobre feriados en Chile. Los datos de feriados se obtienen de una API externa, se transforman y se almacenan en una base de datos SQLite.

## Estructura del Proyecto

```
feriados-api/
├── main.py               # Archivo principal con la lógica de la API y configuración
├── requirements.txt      # Lista de dependencias necesarias
├── feriados.db           # Base de datos SQLite para almacenar los feriados
├── README.md             # Este archivo de documentación
```

## Tecnologías Utilizadas

- Python 3.x
- FastAPI
- SQLite
- Requests (para la consulta a la API externa)
- Uvicorn (como servidor ASGI para FastAPI)

## Requisitos

- Python 3.x o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone <https://github.com/RangerSheff/Python-feriados-chile>
cd Python-feriados-chile
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Para crear un entorno virtual y evitar conflictos con otras dependencias de tu sistema:

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

- **En Windows:**

```bash
venv\Scripts\activate
```

- **En macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

Instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

### 5. Crear la base de datos

El script de la aplicación crea automáticamente la base de datos SQLite y la tabla necesaria si no existen. Si quieres crear la base de datos manualmente, ejecuta el siguiente script SQL:

```sql
CREATE TABLE IF NOT EXISTS feriados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreFeriado TEXT,
    fecha TEXT,
    tipo TEXT,
    descripcion TEXT,
    dia_semana TEXT
);
```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`.

## Uso de la API

La API permite consultar los feriados a través del siguiente endpoint:

- **GET `/feriado/{fecha}`**  
  Consulta los detalles de un feriado para una fecha específica. La fecha debe estar en formato `yyyy-mm-dd`.

### Ejemplo de solicitud

**URL de ejemplo:**

```http
GET http://127.0.0.1:8000/feriado/2024-01-01
```

### Ejemplo de respuesta

```json
{
  "nombreFeriado": "Año Nuevo",
  "fecha": "2024-01-01",
  "tipo": "Civil",
  "descripcion": "Año Nuevo",
  "dia_semana": "Lunes"
}
```

## Documentación de la API

FastAPI genera automáticamente documentación interactiva para tu API. Puedes acceder a ella en las siguientes URLs:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **Redoc UI:** `http://127.0.0.1:8000/redoc`

## Manejo de Errores

La API maneja errores de manera que se devuelve un código de estado adecuado con un mensaje claro.

- Si no se encuentra un feriado para la fecha solicitada, se devolverá un código 404 con el mensaje `"Feriado no encontrado"`.
- En caso de un error interno, se devolverá un código 500 con el mensaje `"Error interno del servidor"`.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tus cambios (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Empuja tus cambios a tu fork (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

```

Este archivo `README.md` tiene toda la información que normalmente se incluiría en un proyecto Python con FastAPI, y está listo para que lo uses en tu repositorio.