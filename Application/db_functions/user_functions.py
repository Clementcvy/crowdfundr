#!/usr/bin/python3

import psycopg2

def delete_user(conn):
    cur = conn.cursor()

    id = input("Entrez l'id de l'utilisateur à supprimer : ")

    sql = "DELETE FROM Contributeur WHERE id=%s"
    try:
        cur.execute(sql, (id,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun utilisateur supprimé.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")

def insert_user(conn):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    nom = input("Entrez le nom de l'utilisateur : ")
    naissance = input("Entrez la date de naissance de l'utilisateur : ")
    pseudo = input("Entrez le pseudo de l'utilisateur : ")
    mail = input("Entrez le mail de l'utilisateur : ")

    sql = "SELECT id FROM Contributeur"
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return
    raw = cur.fetchone()
    max = 0
    while raw:
        if max < raw[0]:
            max = raw[0]
        raw = cur.fetchone()
    id = max + 1

    sql = "INSERT INTO Contributeur (id, nom, naissance, pseudo, mail) VALUES (%s, %s, %s, %s, %s)"

    try:
        cur.execute(sql, (id, nom, naissance, pseudo, mail))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")

def show_users(conn):
    sql = "SELECT * FROM Contributeur ORDER BY id"

    cur = conn.cursor()
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Utilisateurs----")
    while raw:
        print(f"ID : {raw[0]}, Nom : {raw[1]}, Date de naissance : {raw[2]},")
        print(f"Pseudo : {raw[3]}, Mail : {raw[4]}")
        raw = cur.fetchone()
    print("-----------------------")

def update_user(conn):
    cur = conn.cursor()

    id = input("Entrez l'id de l'utilisateur dont les données sont à mettre à jour : ")
    choix = input("Entrez la donnée à modifier (nom, naissance, pseudo, mail) : ")
    if choix not in {"nom", "naissance", "pseudo", "mail"}:
        print("Champ non autorisé")
        return
    value = input("Entrez la nouvelle valeur : ")

    sql = f"UPDATE Contributeur SET {choix}=%s WHERE id=%s"
    try:
        cur.execute(sql, (value, id))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun utilisateur modifié.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
