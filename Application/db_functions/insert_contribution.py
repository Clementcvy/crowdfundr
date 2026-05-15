#!/usr/bin/python3

import psycopg2


def insert_contribution(conn, contributeur):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    print("Voici la liste des projets : ")
    sql = "SELECT id, titre FROM Projet"
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
    raw = cur.fetchone()
    while raw:
        print(f"ID : {raw[0]}, Titre : {raw[1]}")
        raw = cur.fetchone()

    projet = input("Entrez l'id du projet auxquel vous voulez contribuer : ")
    date_c = input("Entrez la date d'aujourd'hui : ")
    montant = input("Entrez le montant de la contribution : ")

    sql = "SELECT id FROM Contribution"
    try:
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)
    raw = cur.fetchone()
    max = 0
    while raw:
        if max < raw[0]:
            max = raw[0]
        raw = cur.fetchone()
    id = max + 1

    sql = "INSERT INTO Contribution (id, date_c, montant, projet, contributeur) VALUES (%s, %s, %s, %s, %s)"

    try:
        cur.execute(sql, (id, date_c, montant, projet, contributeur))
    except psycopg2.Error as e:
        print("Message système :", e)

    conn.commit()
