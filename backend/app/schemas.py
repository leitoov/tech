from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactoCreate(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    celular: Optional[str] = None
    mensaje: Optional[str] = None
    tipo_dispositivo: Optional[str] = None
    campaña: Optional[str] = None