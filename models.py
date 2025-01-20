from pydantic import BaseModel

class Feriado(BaseModel):
    nombreFeriado: str
    fecha: str
    tipo: str
    descripcion: str
    dia_semana: str
