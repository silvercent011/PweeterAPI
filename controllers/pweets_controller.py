from models.Pweet import Pweet

async def createPweet(data):
    pweet_creation = Pweet.create(**data)
    return pweet_creation

async def readPweet(_query):
    pweet_find = Pweet.get(**_query).get()
    return pweet_find

async def deletePweet(_query):
    pweet_find: Pweet = readPweet(_query)
    pweet_find.delete_instance()