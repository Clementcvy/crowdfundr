#!/usr/bin/python3

import psycopg2


def delete_user(conn):
    cur = conn.cursor()

    id = input("Entrez l'id de l'utilisateur à supprimer : ")

    sql = "DELETE FROM Contributeur WHERE id=%s"
    try:
        cur.execute(sql, (id,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun utilisateur supprimé.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
