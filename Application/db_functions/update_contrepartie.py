#!/usr/bin/python3

import psycopg2


def update_contrepartie(conn):
    cur = conn.cursor()

    id = input(
        "Entrez l'id de la contrepartie dont les données sont à mettre à jour : "
    )
    choix = input("Entrez la donnée à modifier : ")
    value = input("Entrez la nouvelle valeur : ")

    sql = "UPDATE Contrepartie_numerique SET %s=%s WHERE id='%s'" % (choix, value, id)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)

    sql = "UPDATE Contrepartie_physique SET %s=%s WHERE id='%s'" % (choix, value, id)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
    conn.commit()
