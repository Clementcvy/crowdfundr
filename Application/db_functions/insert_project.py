#!/usr/bin/python3

import psycopg2


def insert_project(conn):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    titre = input("Entrez le titre du projet : ")
    descr = input("Entrez la description du projet : ")
    objectif = input("Entrez l'objectif du projet : ")
    lancement = input("Entrez la date de lancement du projet : ")
    incubateur = input(
        "Entrez l'incubateur du projet (appuyez sur entrée s'il y en a pas): "
    )
    if incubateur == "":
        incubateur = None

    sql = "SELECT id FROM Projet"
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

    sql = "INSERT INTO Projet (id, titre, descr, objectif, lancement, incubateur) VALUES (%s, %s, %s, %s, %s, %s)"

    try:
        cur.execute(sql, (id, titre, descr, objectif, lancement, incubateur))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
