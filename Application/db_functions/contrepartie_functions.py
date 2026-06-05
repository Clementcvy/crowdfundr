#!/usr/bin/python3

import psycopg2
from db_functions.contribution_functions import show_contributions


def update_contrepartie(conn, contributeur):
    cur = conn.cursor()
    while True:
        id = input("Entrez l'id de la contrepartie (ou 'q' pour quitter) : ")
        if id.lower() == "q":
            break

        sql = "SELECT id_c FROM Contrepartie C JOIN Contribution CO ON C.id_c=CO.id WHERE CO.contributeur=%s AND C.id_c=%s"
        try:
            cur.execute(sql, (contributeur, id))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
        raw = cur.fetchone()
        if not raw:
            print("Cette contrepartie ne vous appartient pas")
            continue

        sql = "SELECT id_c FROM Contrepartie_physique WHERE id_c=%s"
        try:
            cur.execute(sql, (id,))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
        raw = cur.fetchone()
        if raw:
            choix = input(
                "Entrez la donnée à modifier (poids, frais, transporteur) ou 'q' : "
            )
            if choix.lower() == "q":
                break
            if choix not in {"poids", "frais", "transporteur"}:
                print("Champ non autorisé")
                continue
            value = input("Entrez la nouvelle valeur : ")
            sql = f"UPDATE Contrepartie_physique SET {choix}=%s WHERE id_c=%s"
            try:
                cur.execute(sql, (value, id))
            except psycopg2.Error as e:
                print("Message système :", e)
                conn.rollback()
                continue
        else:
            choix = input("Entrez la donnée à modifier (format, taille) ou 'q' : ")
            if choix.lower() == "q":
                break
            if choix not in {"format", "taille"}:
                print("Champ non autorisé")
                continue
            value = input("Entrez la nouvelle valeur : ")
            sql = f"UPDATE Contrepartie_numerique SET {choix}=%s WHERE id_c=%s"
            try:
                cur.execute(sql, (value, id))
            except psycopg2.Error as e:
                print("Message système :", e)
                conn.rollback()
                continue

        if cur.rowcount == 0:
            print("Aucune contrepartie modifiée.")
            conn.rollback()
            continue

        conn.commit()
        print("Opération réussie")
        break
    cur.close()


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
    cur.close()


def show_transporteurs(conn):
    sql = "SELECT nom, delai FROM Transporteur"
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        cur.close()
        return

    raw = cur.fetchone()
    print("-----Transporteurs-----")
    while raw:
        print(f"Nom: {raw[0]}, delai: {raw[1]}")
        raw = cur.fetchone()
    print("-----------------------")
    cur.close()


def insert_contrepartie(conn, contributeur):
    cur = conn.cursor()
    show_contributions(conn, contributeur)

    while True:
        id_c = input("Choisissez l'id de la contribution (ou 'q' pour quitter) : ")
        if id_c.lower() == "q":
            cur.close()
            return

        sql = "SELECT id FROM Contribution WHERE contributeur=%s AND id=%s"
        try:
            cur.execute(sql, (contributeur, id_c))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue

        raw = cur.fetchone()
        if not raw:
            print("Cette contribution ne vous appartient pas")
            continue

        choix = input(
            "1 pour une contrepartie physique, 2 pour une contrepartie numérique : "
        )

        sql = "INSERT INTO Contrepartie VALUES (%s)"
        try:
            cur.execute(sql, (id_c,))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue

        if int(choix) == 1:
            poids = input("Entrez le poids : ")
            frais = input("Entrez les frais : ")
            show_transporteurs(conn)
            transporteur = input("Entrez le transporteur : ")
            sql = "INSERT INTO Contrepartie_physique (id_c, poids, frais, transporteur) VALUES (%s, %s, %s, %s)"
            try:
                cur.execute(sql, (id_c, poids, frais, transporteur))
            except psycopg2.Error as e:
                print("Message système :", e)
                conn.rollback()
                continue
        elif int(choix) == 2:
            format = input("Entrez le format : ")
            taille = input("Entrez la taille : ")
            sql = "INSERT INTO Contrepartie_numerique (id_c, format, taille) VALUES (%s, %s, %s)"
            try:
                cur.execute(sql, (id_c, format, taille))
            except psycopg2.Error as e:
                print("Message système :", e)
                conn.rollback()
                continue
        else:
            print("Choix inconnu.")
            conn.rollback()
            continue

        conn.commit()
        print("Opération réussie")
        break
    cur.close()


def delete_contrepartie(conn, contributeur):
    cur = conn.cursor()
    while True:
        num = input(
            "Entrez l'id de la contrepartie à supprimer (ou 'q' pour quitter) : "
        )
        if num.lower() == "q":
            break

        sql = "SELECT id_c FROM Contrepartie C JOIN Contribution CO ON C.id_c=CO.id WHERE CO.contributeur=%s AND C.id_c=%s"
        try:
            cur.execute(sql, (contributeur, num))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
        raw = cur.fetchone()
        if not raw:
            print("Cette contrepartie ne vous appartient pas")
            continue

        sql = "DELETE FROM Contrepartie_numerique WHERE id_c=%s"
        try:
            cur.execute(sql, (num,))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
        sql = "DELETE FROM Contrepartie_physique WHERE id_c=%s"
        try:
            cur.execute(sql, (num,))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
        sql = "DELETE FROM Contrepartie WHERE id_c=%s"
        try:
            cur.execute(sql, (num,))
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue

        conn.commit()
        print("Opération réussie")
        break
    cur.close()
