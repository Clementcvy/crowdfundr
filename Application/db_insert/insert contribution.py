#!/usr/bin/python3

import psycopg2

HOST = "localhost"
USER = "me"
PASSWORD = "secret"
DATABASE = "mydb"

# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

# Open a cursor to send SQL commands
cur = conn.cursor()

sql = "SELECT id_c FROM Contribution"
cur.execute(sql)

raw = cur.fetchone()
max = 0
while raw:
    if max < raw :
        max = raw
    raw = cur.fetchone()

id = max + 1
date_c = input("Entrez la date de contribution : ")
montant = input("Entrez le montant : ")
projet = input("Entrez le projet : ")
contributeur = input("Entrez le contributeur : ")
sql = "INSERT INTO Contrepartie_numerique (id_c, format, taille) VALUES ('%s', '%s', '%s')" % (id, date_c, montant, projet, contributeur)

cur.execute(sql)

conn.commit()

conn.close()