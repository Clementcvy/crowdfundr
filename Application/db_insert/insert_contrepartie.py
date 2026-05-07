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

choix = input("1 pour une contrepartie physique, 2 pour un contrepartie numérique : ")

sql = "SELECT id_c FROM Contrepartie"
cur.execute(sql)

raw = cur.fetchone()
max = 0
while raw:
    if max < raw :
        max = raw
    raw = cur.fetchone()

id_c = max + 1

if choix == 1:
    format = input("Entrez le format : ")
    taile = input("Entrez la taille : ")
    sql = "INSERT INTO Contrepartie_numerique (id_c, format, taille) VALUES ('%s', '%s', '%s')" % (id_c, format, taille)
if choix == 2:
    poids = input("Entrez le poids : ")
    frais = input("Entrez les frais : ")
    transporteur = input("Entrez le transporteur : ")
    sql = "INSERT INTO Contrepartie_physique (id_c, poids, frais, transporteur) VALUES ('%s', '%s', '%s', '%s')" % (id_c, poids, frais, transporteur)



cur.execute(sql)

conn.commit()

conn.close()