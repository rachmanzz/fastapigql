from dotenv import load_dotenv
from pathlib import Path
load_dotenv(str(Path('.') / '.env'))
from os import getenv
configs = {
    "auth": {
        "default": "jwt",
        "jwt": {
            "secret_key": getenv("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"),
            "algorithm": getenv("algorithm", "HS256"),
            "expire_in_minutes": getenv("token_expire", 30),
            "driver": "orator",
            "provider": {
                "orator": {
                    "driver": "orm-query",
                    "table": "users"
                }
            }
        }
    }
}