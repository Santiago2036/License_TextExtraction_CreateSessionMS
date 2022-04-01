from sqlalchemy import Table,Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine

commissions = Table(
    'commissions',meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('id_entity', Integer, ForeignKey("entitys.id"))
)

meta.create_all(engine)