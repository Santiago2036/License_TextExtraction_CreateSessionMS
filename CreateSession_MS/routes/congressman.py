from fastapi import APIRouter
from config.db import conn
from models.index import congressmans
from schemas.index import Congressman


congressman = APIRouter()

@congressman.get("/")
async def get_users():
    return conn.execute(Congressman.select()).fetchall()


#@user.get("/{id}")
#async def get_user():
#    return conn.execute(users.select().where(users.c.id == id)).fetchall()
#
#
#@user.post("/")
#async def create_user(user: User):
#    new_user = {
#        "name" : user.name,
#        "email" : user.email,
#    }
#    new_user["password"] = funtion_create_password.encrypt(user.password.encode("utf-8"))
#    result = conn.execute(users.insert().values(new_user))
#    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
#
#
#@user.put("/{id}")
#async def update_user(user: User):
#    conn.execute(users.insert().values(
#        name = user.name,
#        email = user.email,
#        password = user.password
#    ))
#    return conn.execute(users.select()).fetchall()
#
#
#@user.delete("/{id}")
#async def delete_user(user: User):
#    conn.execute(users.delete().where)
#    return conn.execute(users.select().where(users.c.id == id)).fetchall()
#