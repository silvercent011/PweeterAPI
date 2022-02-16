from models.User import User
from models.Pweet import Pweet


async def createUser(data):
    user_creation = User.create(**data)
    return user_creation


async def readUser(_query):
    user_find = User.get(**_query).get()
    return user_find


async def updateUser(_query, payload):
    user_update = User.update(**payload).where(**_query).execute()
    return user_update


async def deleteUser(_query):
    user_find: User = readUser(_query)
    user_find.delete_instance()
