from fastapi import APIRouter
from config.db import conn
from models.index import charge_congressmans
from schemas.index import Charge_congressman


charge_congressman = APIRouter()

@charge_congressman.get("/")
async def get_charge_congressman():
    return conn.execute(charge_congressmans.select()).fetchall()
