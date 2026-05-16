#!/usr/bin/python3

import psycopg2


def update_user(conn):
    cur = conn.cursor()

    id = input("Entrez l'id de l'utilisateur dont les données sont à mettre à jour : ")
    choix = input("Entrez la donnée à modifier : ")
    if choix not in {"nom", "naissance", "pseudo", "mail"}:
        print("Champ non autorisé")
        return
    value = input("Entrez la nouvelle valeur : ")

    sql = f"UPDATE Contributeur SET {choix}=%s WHERE id=%s"
    try:
        cur.execute(sql, (value, id))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun utilisateur modifiée.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
