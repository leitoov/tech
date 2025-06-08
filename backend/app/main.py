from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware
from .routers import contacto
from .logging_config import logger
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from .rate_limiter import limiter  # Importar desde el nuevo archivo

# Configuración de la aplicación
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080", "http://localhost:8080", "http://192.168.1.15:8080"],  # URLs permitidas
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

# Configuración de SlowAPI (Rate Limiting)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Incluir routers
app.include_router(contacto.router)

# Registrar un mensaje de inicio
logger.info("Servidor iniciado correctamente")

@app.exception_handler(RateLimitExceeded)
def rate_limit_exceeded_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Demasiadas solicitudes. Por favor, inténtalo de nuevo más tarde."},
    )