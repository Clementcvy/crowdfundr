#!/usr/bin/python3

import psycopg2
from db_functions.show_contribution import show_contributions


def insert_contrepartie(conn, contributeur):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    show_contributions(conn, contributeur)

    id_c = input(
        "Choisissez l'id de le contribution dont vous voulez inserer une contrepartie : "
    )

    sql = "SELECT id FROM Contribution WHERE contributeur=%s AND id=%s"
    try:
        cur.execute(
            sql,
            (
                contributeur,
                id_c,
            ),
        )
    except psycopg2.Error as e:
        print("Message système :", e)

    raw = cur.fetchone()
    if not raw:
        print("Cette contribution ne vous appartient pas")
        return

    choix = input(
        "1 pour une contrepartie physique, 2 pour un contrepartie numérique : "
    )

    sql = "INSERT INTO Contrepartie VALUES (%s)"
    try:
        cur.execute(sql, (id_c,))
    except psycopg2.Error as e:
        print("Message système :", e)

    if int(choix) == 1:
        poids = input("Entrez le poids : ")
        frais = input("Entrez les frais : ")
        transporteur = input("Entrez le transporteur : ")
        sql = "INSERT INTO Contrepartie_physique (id_c, poids, frais, transporteur) VALUES (%s, %s, %s, %s)"

        try:
            cur.execute(
                sql,
                (
                    id_c,
                    poids,
                    frais,
                    transporteur,
                ),
            )
        except psycopg2.Error as e:
            print("Message système :", e)

    elif int(choix) == 2:
        format = input("Entrez le format : ")
        taille = input("Entrez la taille : ")
        sql = "INSERT INTO Contrepartie_numerique (id_c, format, taille) VALUES (%s, %s, %s)"

        try:
            cur.execute(
                sql,
                (
                    id_c,
                    format,
                    taille,
                ),
            )
        except psycopg2.Error as e:
            print("Message système :", e)

    conn.commit()
