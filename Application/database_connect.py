import psycopg2

DATABASE = "dbnf18p080"
USER = "nf18p080"
PASSWORD = "r6zwYwj3X6zW"
HOST = "tuxa.sme.utc"

def connectDatabase():
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    if (conn):
        print("[LOGS] Connexion DB réussie.")
    else:
        print("[LOGS] Connexion DB ratée.")
    return conn

def exitDatabase(conn):
    conn.close()
    print("[LOGS] Connexion SQL fermée.")