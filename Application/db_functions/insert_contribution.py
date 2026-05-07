#!/usr/bin/python3

import psycopg2

def insert_contribution(conn):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    sql = "SELECT id_c FROM Contribution"
    try :
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)
    raw = cur.fetchone()

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

    try :
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)
    raw = cur.fetchone()

    conn.commit()
