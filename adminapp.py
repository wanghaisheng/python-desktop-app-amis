from fastapiHelperadmin import startAmis
from fastapi import FastAPI

adminapp=FastAPI()
startAmis(adminapp,"/amis/set")