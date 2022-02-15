import bcrypt
from fastapi import APIRouter, Body
from controllers.users_controller import createUser, readUser
from models.User import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

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

@router.post('/create')
async def user_auth(request: dict = Body):
    payload = request
    hashedpassword = await hashPassword(payload['password'])
    payload["hashed_password"] = ""
    payload["hashed_password"] = hashedpassword
    payload["password"] = None
    data = createUser(payload)
    return data

@router.post('/auth')
async def user_auth(request: dict = Body):
    payload = request
    data = await readUser({"email":payload['email']})
    passwordEquals = await comparePasswords(payload['password'], data.hashed_password)

    if passwordEquals:
        data.token = ''
        data.hashed_password = None
        return data
    else:
        return False
