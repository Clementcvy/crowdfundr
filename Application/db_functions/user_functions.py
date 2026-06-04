#!/usr/bin/python3

import psycopg2

def delete_user(conn):
    cur = conn.cursor()
    while True:
        show_users(conn)
        id = input("Entrez l'id de l'utilisateur à supprimer (ou 'q' pour annuler) : ")
        if id.lower() == 'q':
            break

        sql = "DELETE FROM Contributeur WHERE id=%s"
        try:
            cur.execute(sql, (id,))
            if cur.rowcount == 0:
                print("Aucun utilisateur supprimé.")
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

def insert_user(conn):
    cur = conn.cursor()
    while True:
        nom = input("Entrez le nom de l'utilisateur (ou 'q' pour annuler) : ")
        if nom.lower() == 'q':
            break
        naissance = input("Entrez la date de naissance de l'utilisateur : ")
        pseudo = input("Entrez le pseudo de l'utilisateur : ")
        mail = input("Entrez le mail de l'utilisateur : ")

        sql = "SELECT MAX(id) FROM Contributeur"
        try:
            cur.execute(sql)
            res = cur.fetchone()
            id = (res[0] + 1) if res[0] is not None else 1

            sql = "INSERT INTO Contributeur (id, nom, naissance, pseudo, mail) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, (id, nom, naissance, pseudo, mail))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()

def show_users(conn):
    sql = "SELECT * FROM Contributeur ORDER BY id"
    cur = conn.cursor()
    try:
        cur.execute(sql)
        raw = cur.fetchone()
        print("-----Utilisateurs----")
        while raw:
            print(f"ID : {raw[0]}, Nom : {raw[1]}, Date de naissance : {raw[2]},")
            print(f"Pseudo : {raw[3]}, Mail : {raw[4]}")
            raw = cur.fetchone()
        print("-----------------------")
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
    cur.close()

def update_user(conn):
    cur = conn.cursor()
    while True:
        show_users(conn)
        id = input("Entrez l'id de l'utilisateur dont les données sont à mettre à jour (ou 'q' pour annuler) : ")
        if id.lower() == 'q':
            break
            
        choix = input("Entrez la donnée à modifier (nom, naissance, pseudo, mail) ou 'q' : ")
        if choix.lower() == 'q':
            break
        if choix not in {"nom", "naissance", "pseudo", "mail"}:
            print("Champ non autorisé")
            continue
            
        value = input("Entrez la nouvelle valeur : ")

        sql = f"UPDATE Contributeur SET {choix}=%s WHERE id=%s"
        try:
            cur.execute(sql, (value, id))
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