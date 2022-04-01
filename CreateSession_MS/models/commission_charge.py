from sqlalchemy import Table,Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

commission_charges = Table(
    'commission_charges',meta,
    Column('id', Integer, primary_key=True),
    Column('id_congressman', Integer, ForeignKey("congressmans.id")),
    Column('id_commission', Integer, ForeignKey("commissions.id")),
    Column('id_charge', Integer, ForeignKey("charge_congressmans.id"))
)

meta.create_all(engine)