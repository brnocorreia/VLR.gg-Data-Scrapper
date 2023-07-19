import psycopg2
from core.configs import postgresql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Importando as variáveis de ambiente do database
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# PsycoPG2
conn = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cur = conn.cursor()

# Using SQLAlchemy
conn_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
db = create_engine(conn_string)
conn_sqlalchemy = db.connect()


