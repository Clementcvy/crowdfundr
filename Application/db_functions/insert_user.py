#!/usr/bin/python3

import psycopg2


def insert_user(conn):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    nom = input("Entrez le nom de l'utilisateur : ")
    naissance = input("Entrez la date de naissance de l'utilisateur : ")
    pseudo = input("Entrez le pseudo de l'utilisateur : ")
    mail = input("Entrez le mail de l'utilisateur : ")

    sql = "SELECT id FROM Contributeur"
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return
    raw = cur.fetchone()
    max = 0
    while raw:
        if max < raw[0]:
            max = raw[0]
        raw = cur.fetchone()
    id = max + 1

    sql = "INSERT INTO Contributeur (id, nom, naissance, pseudo, mail) VALUES (%s, %s, %s, %s, %s)"

    try:
        cur.execute(sql, (id, nom, naissance, pseudo, mail))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
