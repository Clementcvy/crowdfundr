#!/usr/bin/python3

import psycopg2
from datetime import datetime

def update_contribution(conn, contributeur):
    cur = conn.cursor()

    id = input(
        "Entrez l'id de la contribution dont les données sont à mettre à jour : "
    )
    choix = input("Entrez la donnée à modifier (date_c, montant, projet): ")
    if choix not in {"date_c", "montant", "projet"}:
        print("Champ non autorisé")
        return
    value = input("Entrez la nouvelle valeur : ")

    sql = f"UPDATE Contribution SET {choix}=%s WHERE id=%s AND contributeur=%s"
    try:
        cur.execute(sql, (value, id, contributeur))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucune contribution modifiée.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")

def show_contributions(conn, id):
    sql = "SELECT Contribution.id, date_c, montant, projet FROM Contribution JOIN Contributeur ON Contribution.contributeur = Contributeur.id WHERE Contributeur.id = %s"

    cur = conn.cursor()
    try:
        cur.execute(sql, (id,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Contribution----")
    while raw:
        print(f"id: {raw[0]}, date: {raw[1]}, montant: {raw[2]}, projet: {raw[3]}")
        raw = cur.fetchone()
    print("-----------------------")

def insert_contribution(conn, contributeur):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    print("Voici la liste des projets : ")
    sql = "SELECT id, titre FROM Projet"
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return
    raw = cur.fetchone()
    while raw:
        print(f"ID : {raw[0]}, Titre : {raw[1]}")
        raw = cur.fetchone()

    projet = input("Entrez l'id du projet auxquel vous voulez contribuer : ")
    date_c = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    montant = input("Entrez le montant de la contribution : ")

    sql = "SELECT id FROM Contribution"
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

    sql = "INSERT INTO Contribution (id, date_c, montant, projet, contributeur) VALUES (%s, %s, %s, %s, %s)"

    try:
        cur.execute(sql, (id, date_c, montant, projet, contributeur))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")

def delete_contribution(conn, contributeur):
    cur = conn.cursor()

    num = input("Entrez l'id de la contribution à supprimer : ")

    sql = "DELETE FROM Contribution WHERE id=%s AND contributeur=%s"
    try:
        cur.execute(sql, (num, contributeur))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    if cur.rowcount == 0:
        print("Aucune contribution supprimée.")
        conn.rollback()
        return

    conn.commit()
    print("Opération réussie")
