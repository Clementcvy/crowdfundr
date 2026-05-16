#!/usr/bin/python3

import psycopg2


def update_contrepartie(conn, contributeur):
    cur = conn.cursor()

    id = input(
        "Entrez l'id de la contrepartie dont les données sont à mettre à jour : "
    )

    sql = "SELECT id_c FROM Contrepartie C JOIN Contribution CO ON C.id_c=CO.id WHERE CO.contributeur=%s AND C.id_c=%s"
    try:
        cur.execute(
            sql,
            (
                contributeur,
                id,
            ),
        )
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return
    raw = cur.fetchone()
    if not raw:
        print("Cette contrepartie ne vous appartient pas")
        return

    sql = "SELECT id_c FROM Contrepartie_physique WHERE id_c=%s"
    try:
        cur.execute(sql, (id,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return
    raw = cur.fetchone()
    if raw:
        choix = input("Entrez la donnée à modifier (poids, frais, transporteur): ")
        if choix not in {"poids", "frais", "transporteur"}:
            print("Champ non autorisé")
            return
        value = input("Entrez la nouvelle valeur : ")
        sql = f"UPDATE Contrepartie_physique SET {choix}=%s WHERE id_c=%s"
        try:
            cur.execute(
                sql,
                (
                    value,
                    id,
                ),
            )
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            return
    else:
        choix = input("Entrez la donnée à modifier (format, taille): ")
        if choix not in {"format", "taille"}:
            print("Champ non autorisé")
            return
        value = input("Entrez la nouvelle valeur : ")
        sql = f"UPDATE Contrepartie_numerique SET {choix}=%s WHERE id_c=%s"
        try:
            cur.execute(
                sql,
                (
                    value,
                    id,
                ),
            )
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            return

    if cur.rowcount == 0:
        print("Aucune contrepartie modifiée.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
