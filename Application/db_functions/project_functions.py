#!/usr/bin/python3

import psycopg2


def insert_project(conn):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    titre = input("Entrez le titre du projet : ")
    descr = input("Entrez la description du projet : ")
    objectif = input("Entrez l'objectif du projet : ")
    lancement = input("Entrez la date de lancement du projet : ")
    incubateur = input(
        "Entrez l'incubateur du projet (appuyez sur entrée s'il y en a pas): "
    )
    if incubateur == "":
        incubateur = None

    sql = "SELECT id FROM Projet"
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

    sql = "INSERT INTO Projet (id, titre, descr, objectif, lancement, incubateur) VALUES (%s, %s, %s, %s, %s, %s)"

    try:
        cur.execute(sql, (id, titre, descr, objectif, lancement, incubateur))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")

def update_project(conn):
    cur = conn.cursor()

    id = input("Entrez l'id du projet dont les données sont à mettre à jour : ")
    choix = input("Entrez la donnée à modifier (titre, descr, objectif, lancement, incubateur): ")
    if choix not in {"titre", "descr", "objectif", "lancement", "incubateur"}:
        print("Champ non autorisé")
        return
    value = input("Entrez la nouvelle valeur (appuyez sur entrée s'il y en a pas): ")
    if value == "":
        value = None

    sql = f"UPDATE Projet SET {choix}=%s WHERE id=%s"
    try:
        cur.execute(sql, (value, id))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun projet modifié.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")

def show_projects(conn):
    sql = "SELECT * FROM Projet ORDER BY id"

    cur = conn.cursor()
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Projets----")
    while raw:
        print(
            f"ID : {raw[0]}, Titre : {raw[1]}, Description : {raw[2]}, Objectif : {raw[3]},"
        )
        print(f"Date de lancement : {raw[4]}, Incubateur : {raw[5]}")
        raw = cur.fetchone()
    print("-----------------------")

def delete_project(conn):
    cur = conn.cursor()

    id = input("Entrez l'id du projet à supprimer : ")

    sql = "DELETE FROM Projet WHERE id=%s"
    try:
        cur.execute(sql, (id,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucun projet supprimé.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
