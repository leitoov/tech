from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Contacto
from ..schemas import ContactoCreate
from ..rate_limiter import limiter  # Importar desde el nuevo archivo
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/contacto")
@limiter.limit("5/minute")  # Máximo 5 solicitudes por minuto
def crear_contacto(request: Request, contacto: ContactoCreate, db: Session = Depends(get_db)):
    try:
        # Crear el objeto Contacto directamente desde el esquema
        db_contacto = Contacto(**contacto.dict())
        db.add(db_contacto)
        db.commit()
        db.refresh(db_contacto)
        return {"mensaje": "Contacto guardado correctamente"}
    except Exception as e:
        logger.error(f"Error al crear contacto: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")