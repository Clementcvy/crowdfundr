#!/usr/bin/python3

import psycopg2
from db_functions.contribution_functions import show_contributions


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

def show_contreparties(conn, contributeur):
    sql = "SELECT id_c, poids, frais, transporteur FROM Contrepartie_physique CP JOIN Contribution C ON CP.id_c=C.id WHERE C.contributeur=%s"

    cur = conn.cursor()
    try:
        cur.execute(sql, (contributeur,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    raw = cur.fetchone()
    print("-----Contrepartie Physique-----")
    while raw:
        print(
            f"ID_c: {raw[0]}, Poids : {raw[1]}, Frais de livraison : {raw[2]}, Transporteur: {raw[3]}"
        )
        raw = cur.fetchone()
    print("-----------------------")

    sql = "SELECT id_c, format, taille FROM Contrepartie_numerique CN JOIN Contribution C ON CN.id_c=C.id WHERE C.contributeur=%s"
    try:
        cur.execute(sql, (contributeur,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    raw = cur.fetchone()
    print("-----Contrepartie Numérique-----")
    while raw:
        print(f"ID_c: {raw[0]}, Format : {raw[1]}, Taille : {raw[2]}")
        raw = cur.fetchone()
    print("-----------------------")

def insert_contrepartie(conn, contributeur):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    show_contributions(conn, contributeur)

    id_c = input(
        "Choisissez l'id de le contribution dont vous voulez inserer une contrepartie : "
    )

    sql = "SELECT id FROM Contribution WHERE contributeur=%s AND id=%s"
    try:
        cur.execute(
            sql,
            (
                contributeur,
                id_c,
            ),
        )
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    raw = cur.fetchone()
    if not raw:
        print("Cette contribution ne vous appartient pas")
        return

    choix = input(
        "1 pour une contrepartie physique, 2 pour un contrepartie numérique : "
    )

    sql = "INSERT INTO Contrepartie VALUES (%s)"
    try:
        cur.execute(sql, (id_c,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if int(choix) == 1:
        poids = input("Entrez le poids : ")
        frais = input("Entrez les frais : ")
        transporteur = input("Entrez le transporteur : ")
        sql = "INSERT INTO Contrepartie_physique (id_c, poids, frais, transporteur) VALUES (%s, %s, %s, %s)"

        try:
            cur.execute(
                sql,
                (
                    id_c,
                    poids,
                    frais,
                    transporteur,
                ),
            )
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            return

    elif int(choix) == 2:
        format = input("Entrez le format : ")
        taille = input("Entrez la taille : ")
        sql = "INSERT INTO Contrepartie_numerique (id_c, format, taille) VALUES (%s, %s, %s)"

        try:
            cur.execute(
                sql,
                (
                    id_c,
                    format,
                    taille,
                ),
            )
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            return
    else:
        print("Choix inconnu.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")

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
        conn.rollback()
        return
    raw = cur.fetchone()
    if not raw:
        print("Cette contrepartie ne vous appartient pas")
        return

    sql = "DELETE FROM Contrepartie_numerique WHERE id_c=%s"
    try:
        cur.execute(sql, (num,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return
    sql = "DELETE FROM Contrepartie_physique WHERE id_c=%s"
    try:
        cur.execute(sql, (num,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return
    sql = "DELETE FROM Contrepartie WHERE id_c=%s"
    try:
        cur.execute(sql, (num,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
