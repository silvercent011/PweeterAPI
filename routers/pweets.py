from fastapi import APIRouter, Body
from controllers.pweets_controller import createPweet, readPweet
from playhouse.shortcuts import model_to_dict
router = APIRouter(
    prefix="/pweets",
    tags=["pweets"]
)
