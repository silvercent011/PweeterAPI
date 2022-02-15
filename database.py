from peewee import SqliteDatabase, Model

DATABASE_STRING = 'pweeter.db'

db = SqliteDatabase(DATABASE_STRING, check_same_thread=False)

class BaseModel(Model):
    class Meta:
        database = db

