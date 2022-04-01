from fastapi import APIRouter
from config.db import conn
from models.index import commission_charges
from schemas.index import Congressman


commission_charge = APIRouter()

@commission_charge.get("/")
async def get_users():
    return conn.execute(Congressman.select()).fetchall()