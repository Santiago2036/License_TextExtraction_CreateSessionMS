from fastapi import APIRouter
from config.db import conn
from models.index import commissions
from schemas.index import Commission


commission = APIRouter()

@commission.get("/")
async def get_charge_congressman():
    return conn.execute(Commission.select()).fetchall()
