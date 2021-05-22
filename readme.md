# How to Install ?

1. install virtualenv
    - [pip install virtualenv](https://pypi.org/project/virtualenv/)
2. create project direactory 
    - enter your root path of project
    - virtualenv -p python[version] [venv path/dir name]
    - source [venv path/dir name]/bin/activate
3. install fastql packages
    - pip install fastql-packages
4. create new project
    - fastql create [projectname]
5. run your project
    - enter to project directory and run this commandline
    - `fastql run-server --reload`

    note:

    This project use SQL DATABASE with default instalation requirement is "PostgresSQL", you can custom by your self by edit "requirements.txt" dependecies and make sure you have SQL Driver installed in your system.

    - cp ./.env.example ./.env
    - edit .env file. By default, envirotment file store PostgresSQL configuration, custom by your self if you need any extra or change default configs
    - optional: edit configs/database.py

    ```
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
    ```
    if you plan to use postgres as your database drive, you not need to change anything, but if either, follow this setting configuration or make by your self:

    ```
    DATABASES = {
        "default": "mysql",
        "postgres": {
            "driver": "postgres",
            "host": getenv("PG_HOST", "localhost"),
            "database": getenv("PG_DATABASE", "fastql"),
            "user": getenv("PG_USER", "root"),
            "password": getenv("PG_PASSWORD", ""),
            "prefix": getenv("PG_PREFIX", ""),
            "port": getenv("PG_PORT", 5432)
        },
        "mysql": {
            "driver": "mysql",
            "host": getenv("MS_HOST", "localhost"),
            "database": getenv("MS_DATABASE", "localhost"),
            "user": getenv("MS_USER", "root"),
            "password": getenv("MS_PASSWORD", ""),
            "prefix": getenv("MS_PREFIX", "")
        }
    }
    ```
    and make sure, add or edit if you have additional env variables

    the instalation and configuration should be finish here, but if you have any additional configuration, just do that.


# Paths / Directories Structure

```
- app
    - mutations
        - UserMutate.py (example)
    - serializers
        - UserSerialize.py (example)
    - __init__.py
    - mutator.py
    - schema.py
    - start.py
- configs
    - __init__.py
    - database.py
- migrations
- models
- vendor
- .env
- main.py
- requirements.txt
```

- if you want to edit route path or add adddional route, just start from app/start.py. But if you feel that was good enough, you can skip this file.
- app/schema.py, this file prefer to make query schema, so you can custom by your self
- app/mutator.py, this file prefer to build mutation schema, there any addional file from mutations files.
- app/mutations/yourMutate.py, you can create by your own mutation function.
- app/serializers/yourSerialize.py, you can create by your own serialize class and function.


# Databases

Orator ORM, in this project, we use orator ORM to process any SQL databse. You can read [docs](https://orator-orm.com/docs/orm.html) to see how orator work

- create model and migration
    ``` 
        orator make:model [yourModelName] -m
    ```

# Run your Your GrapthQL Project
    uvicorn main:app --reload



