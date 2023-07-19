import os
from dotenv import load_dotenv

# Importando as variáveis de ambiente do database
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Dicionário referente ao banco de dados PostgreSQL

postgresql = {
    'pguser': DB_USER,
    'pgpassword': DB_PASSWORD,
    'pghost': DB_HOST,
    'pgport': DB_PORT,
    'pgname': DB_NAME,
}
