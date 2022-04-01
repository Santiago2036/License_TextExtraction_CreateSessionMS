import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine, MetaData

nameBD = os.getenv("DB_NAME")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
engine = create_engine("mysql+pymysql://"+user+":"+password+"@"+host+":3306/"+nameBD)
meta = MetaData()
conn = engine.connect()