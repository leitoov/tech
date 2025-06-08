from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from .db import Base
from datetime import datetime

class Contacto(Base):
    __tablename__ = "contactos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    celular = Column(String(30))
    mensaje = Column(Text)
    tipo_dispositivo = Column(String(50))
    campaña = Column(String(100))
    fecha_creado = Column(TIMESTAMP, default=datetime.utcnow)
