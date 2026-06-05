#!/usr/bin/python3

import psycopg2
from datetime import datetime

def update_contribution(conn, contributeur):
    cur = conn.cursor()
    while True:
        show_contributions(conn, contributeur)
        id = input("Entrez l'id de la contribution à mettre à jour (ou 'q' pour annuler) : ")
        if id.lower() == 'q':
            break
        
        choix = input("Entrez la donnée à modifier (date_c, montant, projet) ou 'q' : ")
        if choix.lower() == 'q':
            break
        if choix not in {"date_c", "montant", "projet"}:
            print("Champ non autorisé")
            continue
            
        value = input("Entrez la nouvelle valeur : ")

        sql = f"UPDATE Contribution SET {choix}=%s WHERE id=%s AND contributeur=%s"
        try:
            cur.execute(sql, (value, id, contributeur))
            if cur.rowcount == 0:
                print("Aucune contribution modifiée.")
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

def show_contributions(conn, id):
    sql = "SELECT Contribution.id, date_c, montant, projet FROM Contribution JOIN Contributeur ON Contribution.contributeur = Contributeur.id WHERE Contributeur.id = %s"
    cur = conn.cursor()
    try:
        cur.execute(sql, (id,))
        raw = cur.fetchone()
        print("-----Contribution----")
        while raw:
            print(f"id: {raw[0]}, date: {raw[1]}, montant: {raw[2]}, projet: {raw[3]}")
            raw = cur.fetchone()
        print("-----------------------")
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
    cur.close()

def insert_contribution(conn, contributeur):
    cur = conn.cursor()
    while True:
        print("Voici la liste des projets : ")
        sql = "SELECT id, titre FROM Projet"
        try:
            cur.execute(sql)
            raw = cur.fetchone()
            while raw:
                print(f"ID : {raw[0]}, Titre : {raw[1]}")
                raw = cur.fetchone()
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            cur.close()
            return

        projet = input("Entrez l'id du projet (ou 'q' pour annuler) : ")
        if projet.lower() == 'q':
            break
            
        date_c = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        montant = input("Entrez le montant de la contribution : ")

        sql = "SELECT MAX(id) FROM Contribution"
        try:
            cur.execute(sql)
            res = cur.fetchone()
            new_id = (res[0] + 1) if res[0] is not None else 1
            
            sql_insert = "INSERT INTO Contribution (id, date_c, montant, projet, contributeur) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql_insert, (new_id, date_c, montant, projet, contributeur))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()

def delete_contribution(conn, contributeur):
    cur = conn.cursor()
    while True:
        show_contributions(conn, contributeur)
        num = input("Entrez l'id de la contribution à supprimer (ou 'q' pour annuler) : ")
        if num.lower() == 'q':
            break

        sql = "DELETE FROM Contribution WHERE id=%s AND contributeur=%s"
        try:
            cur.execute(sql, (num, contributeur))
            if cur.rowcount == 0:
                print("Aucune contribution supprimée.")
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