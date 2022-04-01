from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine

sessions = Table(
    'sessions',meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('date_initial', String(255)),    
    Column('data_final', String(255)),
    Column('audio_link', String(255)),
    Column('video_link', String(255)),
    Column('pk_Commission', String(255)),
)

meta.create_all(engine)