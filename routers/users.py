from fastapi import APIRouter, Body
from functions.utils import hashPassword, comparePasswords, encodeToken
from controllers.users_controller import createUser, readUser
from playhouse.shortcuts import model_to_dict
import json
router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post('/create')
async def user_auth(request: dict = Body):
    payload = request
    hashedpassword = await hashPassword(payload['password'])
    payload["hashed_password"] = hashedpassword
    payload["password"] = None
    data = createUser(payload)
    data = model_to_dict(data)
    data['token'] = await encodeToken(json.loads(json.dumps(data, default=str)))
    return data


@router.post('/auth')
async def user_auth(request: dict = Body):
    payload = request
    data = await readUser({"email": payload['email']})
    pweets = []
    passwordEquals = await comparePasswords(payload['password'], data.hashed_password)

    if passwordEquals:
        for pweet in data.pweets:
            pweets.append(model_to_dict(pweet))
        data = model_to_dict(data)
        del data['hashed_password']
        data['pweets'] = pweets
        data['token'] = await encodeToken(json.loads(json.dumps(data, default=str)))
        return data
    else:
        return False
