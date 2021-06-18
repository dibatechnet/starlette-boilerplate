from starlette.config import Config
from databases import DatabaseURL

config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=True)

DATABASE_URL = config('DATABASE_URL', cast=DatabaseURL, default="mongodb://localhost:27017")
