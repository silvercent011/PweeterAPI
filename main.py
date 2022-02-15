# General Imports
from manageDB import ManageDB
from fastapi import FastAPI
import os
#dotenv
from dotenv import dotenv_values
config = dotenv_values(".env")
# Import Routers
from routers import users


# Creating Database Tables
ManageDB()


# Starting FastAPI
app = FastAPI()


# Including Router
app.include_router(users.router)


@app.get('/')
async def root():
    return {"message": "server is running"}
