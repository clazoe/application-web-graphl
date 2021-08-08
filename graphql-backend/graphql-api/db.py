from orator import DatabaseManager, Schema, Model
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "db",
        "database": "graphql_db_test",
        "user": "postgres",
        "password": "admin",
        "prefix": "",
        "port": 5432
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)