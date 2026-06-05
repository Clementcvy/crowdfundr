#!/usr/bin/python3

import psycopg2
from db_functions.contrepartie_functions import show_transporteurs


def delete_transporteur(conn):
    cur = conn.cursor()
    while True:
        show_transporteurs(conn)
        nom = input(
            "Entrez le nom du transporteur à supprimer (ou 'q' pour annuler) : "
        )
        if nom.lower() == "q":
            break

        sql = "DELETE FROM Transporteur WHERE nom=%s"
        try:
            cur.execute(sql, (nom,))
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


def insert_transporteur(conn):
    cur = conn.cursor()
    while True:
        nom = input("Entrez le nom du transporteur (ou 'q' pour annuler) : ")
        if nom.lower() == "q":
            break
        delai = input("Entrez le delai du transporteur : ")

        try:
            sql = "INSERT INTO Transporteur (nom, delai) VALUES (%s, %s)"
            cur.execute(sql, (nom, delai))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()


def update_transporteur(conn):
    cur = conn.cursor()
    while True:
        show_transporteurs(conn)
        nom = input(
            "Entrez le nom du transporteur dont les données sont à mettre à jour (ou 'q' pour annuler) : "
        )
        if nom.lower() == "q":
            break

        choix = input("Entrez la donnée à modifier (nom, delai) ou 'q' : ")
        if choix.lower() == "q":
            break
        if choix not in {"nom", "delai"}:
            print("Champ non autorisé")
            continue

        value = input("Entrez la nouvelle valeur : ")

        sql = f"UPDATE Transporteur SET {choix}=%s WHERE nom=%s"
        try:
            cur.execute(sql, (value, nom))
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
