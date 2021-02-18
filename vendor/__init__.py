from app.application import app as application
import app.start
from orator import DatabaseManager, Schema, Model
from configs.database import config as dbConfig
db = DatabaseManager(dbConfig)
schema = Schema(db)
Model.set_connection_resolver(db)
app = application
