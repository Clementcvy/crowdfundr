#!/usr/bin/python3

import psycopg2


def update_project(conn):
    cur = conn.cursor()

    id = input("Entrez l'id du projet dont les données sont à mettre à jour : ")
    choix = input("Entrez la donnée à modifier : ")
    if choix not in {"titre", "descr", "objectif", "lancement", "incubateur"}:
        print("Champ non autorisé")
        return
    value = input("Entrez la nouvelle valeur (appuyez sur entrée s'il y en a pas): ")
    if value == "":
        value = None

    sql = f"UPDATE Projet SET {choix}=%s WHERE id=%s"
    try:
        cur.execute(sql, (value, id))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun projet modifié.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
