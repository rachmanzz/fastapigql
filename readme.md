# How to Install ?

This project running well on python >=3.6.

This Project is under development and not documented well, some file may missing or need create manually

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


# Paths / Directories Structure

```
- app
    - mutations
        - user_mutation.py (example)
    - serializers
        - user_serialize.py (example)
    - __init__.py
    - mutation_schema.py
    - queries_schema.py
    - start.py
- configs
    - __init__.py
    - database.py
- migrations
- models
- .env
- main.py
```

- if you want to edit route path or add adddional route, just start from app/start.py. But if you feel that was good enough, you can skip this file.
- app/queries_schema.py, this file prefer to make query schema, so you can custom by your self
- app/mutation_schema.py, this file prefer to build mutation schema, there any addional file from mutations files.
- app/mutations/yourfile_mutatio.py, you can create by your own mutation function.
- app/serializers/yourfile_serialize.py, you can create by your own serialize class and function.


# Databases

In this project, we use orator ORM to process any SQL database. You can read [docs](https://orator-orm.com/docs/orm.html) to see how orator work:

- make model
    ``` 
    fastql make model --name [modelName]
    ```

    option:
    - `-m` or `--migration`: auto create migration
    - `-s` or `--serialize`: auto create serialize file
    - `-a` or `--all`: auto migration and serialize file
- make migration
    ``` 
    fastql make migration --name [migrationName]
    ```

    option:
    - `-t` or `--table`: define table name

- make serialize file
    ``` 
    fastql make serialize --name [serializeName]
    ```

- make mutation
    ``` 
    fastql make mutation --name [mutationName]
    ```

    option:
    - `-d` or `--depend`: serialize file name
    - `--arg-key`: define argument that referance to your input serialize file


# Migration

- migration commandline

    - `fastql migrate`
    - `fastql migrate --rollback`
    - `fastql migrate --reset`
    - `fastql migrate --status`

# Run your Your GraphQL Project
    
`fastql run-server`



