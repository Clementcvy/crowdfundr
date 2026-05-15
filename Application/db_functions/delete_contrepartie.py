#!/usr/bin/python3

import psycopg2


def delete_contrepartie(conn):
    cur = conn.cursor()

    num = input("Entrez l'id de la contrepartie à supprimer : ")

    sql = "DELETE FROM Contrepartie_numerique WHERE id_c='%s'" % (num)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
    sql = "DELETE FROM Contrepartie_physique WHERE id_c='%s'" % (num)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
    sql = "DELETE FROM Contrepartie WHERE id_c='%s'" % (num)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
    conn.commit()
