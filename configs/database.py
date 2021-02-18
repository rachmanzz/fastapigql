from os import getenv
config = {
    "default": getenv("DB_DRIVER", "postgres"),
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