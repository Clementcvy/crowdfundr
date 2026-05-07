#!/usr/bin/python3

# http://initd.org/psycopg/docs/usage.html

import psycopg2

def print_personne(conn):
    # Open a cursor to send SQL commands
    cur = conn.cursor()

    id = input("Entrez l'id de la personne dont vous voulez les informations : ")

    # Execute a SQL SELECT command
    sql = "SELECT * FROM Membre WHERE id = '%s'", % (id)
    try :
        cur.execute(sql)

        # Fetch data line by line
        raw = cur.fetchone()
        print("C'est un membre de projet")
        while raw:
            print (raw[0])
            print (raw[1])
            print (raw[2])
            print (raw[3])
            print (raw[4])
            raw = cur.fetchone()
    except psycopg2.IntegrityError as e:
        print("Message système :", e)

    sql = "SELECT * FROM Contributeur WHERE id = '%s'", % (id)
    try :
        cur.execute(sql)

        # Fetch data line by line
        raw = cur.fetchone()
        print("C'est un contributeur")
        while raw:
            print (raw[0])
            print (raw[1])
            print (raw[2])
            print (raw[3])
            print (raw[4])
            raw = cur.fetchone()
    except psycopg2.IntegrityError as e:
        print("Message système :", e)

