import datetime
from peewee import CharField, DateField
from database import BaseModel

class User(BaseModel):
    name = CharField()
    user_name = CharField()
    email = CharField(unique=True)
    hashed_password = CharField()
    created_at = DateField(default=datetime.datetime.now)
    updated_at = DateField()

    def save(self, force_insert=False, only=None):
        self.updated_at = datetime.datetime.now()
        return super().save(force_insert, only)