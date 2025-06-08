import logging
from logging.handlers import RotatingFileHandler
import os

# Asegúrate de que la carpeta de logs exista
LOG_DIR = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "backend.log")

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,  # Nivel de log (INFO, DEBUG, ERROR, etc.)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=1000000, backupCount=3),  # Rotación de logs
        logging.StreamHandler()  # Mostrar logs en la consola
    ],
)

logger = logging.getLogger("backend")