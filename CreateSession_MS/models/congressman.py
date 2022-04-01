from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine

congressmans = Table(
    'congressmans',meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(50)),
    Column('email', String(50)),
    Column('phone', String(255)),
    Column('gender', String(255)),
    Column('path_photo', String(255))
)

meta.create_all(engine)