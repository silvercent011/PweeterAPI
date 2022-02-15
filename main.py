# General Imports
from manageDB import ManageDB
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
#dotenv
from dotenv import dotenv_values
config = dotenv_values(".env")
# Import Routers
from routers import users,pweets


# Creating Database Tables
ManageDB()


# Starting FastAPI
app = FastAPI()

#cors
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Including Router
app.include_router(users.router)
app.include_router(pweets.router)


@app.get('/')
async def root():
    return {"message": "server is running"}
