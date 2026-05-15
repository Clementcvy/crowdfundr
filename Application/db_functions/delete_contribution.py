#!/usr/bin/python3

import psycopg2


def delete_contribution(conn):
    cur = conn.cursor()

    num = input("Entrez l'id de la contribution à supprimer : ")

    sql = "DELETE FROM Contribution WHERE id='%s'" % (num)
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
    conn.commit()
