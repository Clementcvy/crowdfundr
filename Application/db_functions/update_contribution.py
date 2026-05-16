#!/usr/bin/python3

import psycopg2


def update_contribution(conn, contributeur):
    cur = conn.cursor()

    id = input(
        "Entrez l'id de la contribution dont les données sont à mettre à jour : "
    )
    choix = input("Entrez la donnée à modifier : ")
    if choix not in {"date_c", "montant", "projet"}:
        print("Champ non autorisé")
        return
    value = input("Entrez la nouvelle valeur : ")

    sql = f"UPDATE Contribution SET {choix}=%s WHERE id=%s AND contributeur=%s"
    try:
        cur.execute(sql, (value, id, contributeur))
    except psycopg2.Error as e:
        print("Message système :", e)

    print("Opération réussie")
    conn.commit()
