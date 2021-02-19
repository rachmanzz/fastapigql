from orator import DatabaseManager, Schema, Model
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(str(Path('.') / '.env'))
from os import getenv

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": getenv("PG_HOST", "localhost"),
        "database": getenv("PG_DATABASE", "fastql"),
        "user": getenv("PG_USER", "root"),
        "password": getenv("PG_PASSWORD", ""),
        "prefix": getenv("PG_PREFIX", ""),
        "port": getenv("PG_PORT", 5432)
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)