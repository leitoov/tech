from slowapi import Limiter
from slowapi.util import get_remote_address

# Configuración de SlowAPI
limiter = Limiter(key_func=get_remote_address)