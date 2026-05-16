#!/usr/bin/python3

import psycopg2


def delete_contrepartie(conn, contributeur):
    cur = conn.cursor()

    num = input("Entrez l'id de la contrepartie à supprimer : ")

    sql = "SELECT id_c FROM Contrepartie C JOIN Contribution CO ON C.id_c=CO.id WHERE CO.contributeur=%s AND C.id_c=%s"
    try:
        cur.execute(
            sql,
            (
                contributeur,
                num,
            ),
        )
    except psycopg2.Error as e:
        print("Message système :", e)
    raw = cur.fetchone()
    if not raw:
        print("Cette contrepartie ne vous appartient pas")
        return

    sql = "DELETE FROM Contrepartie_numerique WHERE id_c=%s"
    try:
        cur.execute(sql, (num,))
    except psycopg2.Error as e:
        print("Message système :", e)
    sql = "DELETE FROM Contrepartie_physique WHERE id_c=%s"
    try:
        cur.execute(sql, (num,))
    except psycopg2.Error as e:
        print("Message système :", e)
    sql = "DELETE FROM Contrepartie WHERE id_c=%s"
    try:
        cur.execute(sql, (num,))
    except psycopg2.Error as e:
        print("Message système :", e)
    conn.commit()
