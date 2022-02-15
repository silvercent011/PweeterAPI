from models.User import User


def createUser(data):
    user_creation = User.create(**data)
    return user_creation


async def readUser(_query):
    user_find = User.get(**_query).get()
    return user_find


async def updateUser():
    pass


async def deleteUser():
    pass
