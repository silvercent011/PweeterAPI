import bcrypt
import os
from jwt import encode,decode

async def hashPassword(password: str):
    pssw = password.encode('utf-8')
    hashed = bcrypt.hashpw(pssw, bcrypt.gensalt(10))
    return hashed

async def comparePasswords(password: str, hashed: str):
    pssw = password.encode('utf-8')
    hsd = hashed.encode('utf-8')

    if bcrypt.checkpw(pssw, hsd):
        return True
    else:
        return False

async def encodeToken(user):
    SECRET = os.environ.get("JWT_SECRET")
    token = encode(user,SECRET, algorithm="HS256")
    return token

async def decodeToken(token):
    SECRET = os.environ.get("JWT_SECRET")
    decoded_token = decode(token, SECRET, algorithms=["HS256"])
    return decoded_token