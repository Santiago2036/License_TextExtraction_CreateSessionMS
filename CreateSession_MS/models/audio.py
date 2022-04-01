from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine

congressmans = Table(
    'commission',meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('id_session', String(255)),    
    Column('link', String(255)),
    Column('audio_link', String(255))
)

meta.create_all(engine)