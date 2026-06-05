#!/usr/bin/python3

import psycopg2


def show_ong(conn):
    sql = "SELECT NEU, nom, pays FROM ONG"
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        cur.close()
        return

    raw = cur.fetchone()
    print("----------ONG----------")
    while raw:
        print(f"NEU: {raw[0]}, nom: {raw[1]}, pays: {raw[2]}")
        raw = cur.fetchone()
    print("-----------------------")
    cur.close()


def delete_ong(conn):
    cur = conn.cursor()
    while True:
        show_ong(conn)
        neu = input("Entrez le NEU de l'ONG à supprimer (ou 'q' pour annuler) : ")
        if neu.lower() == "q":
            break

        sql = "DELETE FROM ONG WHERE NEU=%s"
        try:
            cur.execute(sql, (neu,))
            if cur.rowcount == 0:
                print("Aucun transporteur supprimé.")
                conn.rollback()
            else:
                conn.commit()
                print("Opération réussie")
                break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()


def insert_ong(conn):
    cur = conn.cursor()
    while True:
        neu = input("Entrez le neu de l'ONG (ou 'q' pour annuler) : ")
        if neu.lower() == "q":
            break
        nom = input("Entrez le nom de l'ONG : ")
        pays = input("Entrez le pays de l'ONG : ")

        try:
            sql = "INSERT INTO ONG (NEU, nom, pays) VALUES (%s, %s, %s)"
            cur.execute(sql, (neu, nom, pays))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()


def update_ong(conn):
    cur = conn.cursor()
    while True:
        show_ong(conn)
        neu = input(
            "Entrez le NEU le l'ONG dont les données sont à mettre à jour (ou 'q' pour annuler) : "
        )
        if neu.lower() == "q":
            break

        choix = input("Entrez la donnée à modifier (NEU, nom, pays) ou 'q' : ")
        if choix.lower() == "q":
            break
        if choix not in {"NEU", "nom", "pays"}:
            print("Champ non autorisé")
            continue

        value = input("Entrez la nouvelle valeur : ")

        sql = f"UPDATE ONG SET {choix}=%s WHERE NEU=%s"
        try:
            cur.execute(sql, (value, neu))
            if cur.rowcount == 0:
                print("Aucun utilisateur modifié.")
                conn.rollback()
            else:
                conn.commit()
                print("Opération réussie")
                break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()
