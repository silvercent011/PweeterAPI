from peewee import SqliteDatabase, Model

DATABASE_STRING = 'pweeter.db'

db = SqliteDatabase(DATABASE_STRING)

class BaseModel(Model):
    class Meta:
        database = db

