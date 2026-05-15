#!/usr/bin/python3

import psycopg2


def update_contribution(conn):
    cur = conn.cursor()

    id = input(
        "Entrez l'id de la contribution dont les données sont à mettre à jour : "
    )
    choix = input("Entrez la donnée à modifier : ")
    value = input("Entrez la nouvelle valeur : ")

    sql = "UPDATE Contribution SET %s=%s WHERE id='%s'" % (choix, value, id)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
    conn.commit()
