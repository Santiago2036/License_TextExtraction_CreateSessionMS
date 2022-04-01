from fastapi import APIRouter
from config.db import conn
from models.index import entitys
from schemas.index import Entity


entity = APIRouter()

@entity.get("/")
async def get_charge_congressman():
    return conn.execute(Entity.select()).fetchall()
