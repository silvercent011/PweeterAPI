from fastapi import APIRouter, Body
from controllers.pweets_controller import createPweet, readPweet
from playhouse.shortcuts import model_to_dict
router = APIRouter(
    prefix="/pweets",
    tags=["pweets"]
)

@router.post('/create')
async def create_pweet(request: dict = Body):
    payload = request
    data = await createPweet(payload)
    data = model_to_dict(data)
    return data
