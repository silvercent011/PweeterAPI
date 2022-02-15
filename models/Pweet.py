import datetime
from peewee import CharField, DateField, ForeignKeyField
from database import BaseModel

from models import User

class Pweet(BaseModel):
    text = CharField()
    user = ForeignKeyField(User.User, backref='pweets')
    created_at = DateField(default=datetime.datetime.now)