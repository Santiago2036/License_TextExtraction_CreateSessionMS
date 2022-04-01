from fastapi import FastAPI
from routes.index import *
app = FastAPI()

app.include_router(entity)
app.include_router(commission)
app.include_router(congressman)
app.include_router(charge_congressman)
app.include_router(commission_charge)
