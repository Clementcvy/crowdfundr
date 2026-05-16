#!/usr/bin/python3

import psycopg2


def delete_contribution(conn, contributeur):
    cur = conn.cursor()

    num = input("Entrez l'id de la contribution à supprimer : ")

    sql = "DELETE FROM Contribution WHERE id=%s AND contributeur=%s"
    try:
        cur.execute(sql, (num, contributeur))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucune contribution supprimée.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
