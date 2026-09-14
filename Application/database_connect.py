import os

import psycopg2

DATABASE = os.getenv("CROWDFUNDR_DB_NAME", "crowdfundr")
USER = os.getenv("CROWDFUNDR_DB_USER", "crowdfundr")
PASSWORD = os.getenv("CROWDFUNDR_DB_PASSWORD", "crowdfundr")
HOST = os.getenv("CROWDFUNDR_DB_HOST", "localhost")
PORT = os.getenv("CROWDFUNDR_DB_PORT", "5432")
SCHEMA = os.getenv("CROWDFUNDR_DB_SCHEMA", "sql")

def connectDatabase():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        options=f"-c search_path={SCHEMA}"
    )
    if (conn):
        print("[LOGS] Connexion DB réussie.")
    else:
        print("[LOGS] Connexion DB ratée.")
    return conn

def exitDatabase(conn):
    conn.close()
    print("[LOGS] Connexion SQL fermée.")
