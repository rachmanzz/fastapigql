from os import getenv
driver_init = {
    "postgres": {
        "postgres": {
            "driver": "postgres",
            "host": getenv("DB_HOST", "localhost"),
            "database": getenv("DB_DATABASE", "fastql"),
            "user": getenv("DB_USER", "root"),
            "password": getenv("DB_PASSWORD", ""),
            "prefix": getenv("DB_PREFIX", ""),
            "port": getenv("DB_PORT", 5432)
        }
    }
}

DB_DRIVER[getenv("DB_DRIVER", "postgres")]