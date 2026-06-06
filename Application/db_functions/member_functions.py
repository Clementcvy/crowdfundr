#!/usr/bin/python3

import psycopg2

def delete_member(conn):
    cur = conn.cursor()
    while True:
        show_members(conn)
        id = input("Entrez l'id du membre à supprimer (ou 'q' pour annuler) : ")
        if id.lower() == 'q':
            break

        sql = "DELETE FROM Membre WHERE id=%s"
        try:
            cur.execute(sql, (id,))
            if cur.rowcount == 0:
                print("Aucun membre supprimé.")
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

def insert_member(conn):
    cur = conn.cursor()
    while True:
        nom = input("Entrez le nom du membre (ou 'q' pour annuler) : ")
        if nom.lower() == 'q':
            break
        prenom = input("Entrez le prenom du membre : ")
        naissance = input("Entrez la date de naissance du membre : ")
        pays = input("Entrez le pays du membre : ")

        sql = "SELECT MAX(id) FROM Membre"
        try:
            cur.execute(sql)
            res = cur.fetchone()
            id = (res[0] + 1) if res[0] is not None else 1

            sql = "INSERT INTO Membre (id, nom, naissance, prenom, pays) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, (id, nom, naissance, prenom, pays))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()

def show_members(conn):
    sql = "SELECT * FROM Membre ORDER BY id"
    cur = conn.cursor()
    try:
        cur.execute(sql)
        raw = cur.fetchone()
        print("-----Membres----")
        while raw:
            print(f"ID : {raw[0]}, Nom : {raw[1]}, Date de naissance : {raw[2]},")
            print(f"Prenom : {raw[3]}, Pays : {raw[4]}")
            raw = cur.fetchone()
        print("-----------------------")
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
    cur.close()

def update_member(conn):
    cur = conn.cursor()
    while True:
        show_members(conn)
        id = input("Entrez l'id du membre dont les données sont à mettre à jour (ou 'q' pour annuler) : ")
        if id.lower() == 'q':
            break
        choix = input("Entrez la donnée à modifier (nom, naissance, prenom, pays) ou 'q' : ")
        if choix.lower() == 'q':
            break
        if choix not in {"nom", "naissance", "prenom", "pays"}:
            print("Champ non autorisé")
            continue
            
        value = input("Entrez la nouvelle valeur : ")

        sql = f"UPDATE Membre SET {choix}=%s WHERE id=%s"
        try:
            cur.execute(sql, (value, id))
            if cur.rowcount == 0:
                print("Aucun membre modifié.")
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