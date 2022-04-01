from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine

entitys = Table(
    'entitys',meta,
    Column('id', Integer, primary_key=True),
    Column('name_entity', String(255))
)

meta.create_all(engine)