from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine

charge_congressmans = Table(
    'charge_congressmans',meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)

meta.create_all(engine)