#!/usr/bin/python3

import psycopg2


def delete_project(conn):
    cur = conn.cursor()

    id = input("Entrez l'id du projet à supprimer : ")

    sql = "DELETE FROM Projet WHERE id=%s"
    try:
        cur.execute(sql, (id,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun projet supprimé.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
