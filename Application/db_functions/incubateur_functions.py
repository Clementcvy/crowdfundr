#!/usr/bin/python3

import psycopg2


def show_incubateur(conn):
    sql = "SELECT nom, creation, budget FROM Incubateur"
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        cur.close()
        return

    raw = cur.fetchone()
    print("----------Incubateur----------")
    while raw:
        print(f"nom: {raw[0]}, creation: {raw[1]}, budget: {raw[2]}")
        raw = cur.fetchone()
    print("-----------------------")
    cur.close()


def delete_incubateur(conn):
    cur = conn.cursor()
    while True:
        show_incubateur(conn)
        nom = input(
            "Entrez le nom de l'incubateur à supprimer (ou 'q' pour annuler) : "
        )
        if nom.lower() == "q":
            break

        sql = "DELETE FROM Incubateur WHERE nom=%s"
        try:
            cur.execute(sql, (nom,))
            if cur.rowcount == 0:
                print("Aucun incubateur supprimé.")
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


def insert_incubateur(conn):
    cur = conn.cursor()
    while True:
        nom = input("Entrez le nom de l'incubateur (ou 'q' pour annuler) : ")
        if nom.lower() == "q":
            break
        creation = input("Entrez la creation de l'incubateur : ")
        budget = input("Entrez le budget de l'incubateur : ")

        try:
            sql = "INSERT INTO Incubateur (nom, creation, budget) VALUES (%s, %s, %s)"
            cur.execute(sql, (nom, creation, budget))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()


def update_incubateur(conn):
    cur = conn.cursor()
    while True:
        show_incubateur(conn)
        nom = input(
            "Entrez le nom le l'incubateur dont les données sont à mettre à jour (ou 'q' pour annuler) : "
        )
        if nom.lower() == "q":
            break

        choix = input("Entrez la donnée à modifier (nom, creation, budget) ou 'q' : ")
        if choix.lower() == "q":
            break
        if choix not in {"nom", "creation", "budget"}:
            print("Champ non autorisé")
            continue

        value = input("Entrez la nouvelle valeur : ")

        sql = f"UPDATE Incubateur SET {choix}=%s WHERE nom=%s"
        try:
            cur.execute(sql, (value, nom))
            if cur.rowcount == 0:
                print("Aucun incubateur modifié.")
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
