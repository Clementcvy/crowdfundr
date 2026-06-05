#!/usr/bin/python3

import psycopg2

def show_incubateurs(conn):
    sql = "SELECT * FROM Incubateur"
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()

    raw = cur.fetchone()
    print("-----Incubateurs-----")
    while raw:
        print(
            f"Nom: {raw[0]}, Création: {raw[1]}, Budget {raw[2]}"
        )
        raw = cur.fetchone()
    print("-----------------------")
    cur.close()

def insert_project(conn):
    cur = conn.cursor()
    while True:
        titre = input("Entrez le titre du projet (ou 'q' pour annuler) : ")
        if titre.lower() == 'q':
            break
        descr = input("Entrez la description du projet : ")
        objectif = input("Entrez l'objectif du projet : ")
        lancement = input("Entrez la date de lancement du projet : ")
        show_incubateurs(conn)
        incubateur = input("Entrez l'incubateur du projet (appuyez sur entrée s'il y en a pas) : ")
        if incubateur == "":
            incubateur = None

        type_projet = input("Entrez le type du projet (Projet social : 1, Projet techno : 2, Projet artis : 3) : ")

        if int(type_projet) not in (1, 2, 3):
            print("Message système : Option non possible.")
            continue

        match int(type_projet):
            case 1:
                region = input("Entrez la région : ")
            case 2:
                innovation = input("Entrez l'innovation : ")
            case 3:
                medium = input("Entrez le médium : ")

        sql = "SELECT MAX(id) FROM Projet"
        try:
            cur.execute(sql)
            res = cur.fetchone()
            id = (res[0] + 1) if res[0] is not None else 1
            
            sql = "INSERT INTO Projet (id, titre, descr, objectif, lancement, incubateur) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(sql, (id, titre, descr, objectif, lancement, incubateur))
            
            match int(type_projet):
                case 1:
                    cur.execute("INSERT INTO Projet_social (id_p, region) VALUES (%s, %s)", (id, region))
                case 2:
                    cur.execute("INSERT INTO Projet_techno (id_p, innovation) VALUES (%s, %s)", (id, innovation))
                case 3:
                    cur.execute("INSERT INTO Projet_artis (id_p, medium) VALUES (%s, %s)", (id, medium))
            
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()

def update_project(conn):
    cur = conn.cursor()
    while True:
        id = input("Entrez l'id du projet à mettre à jour (ou 'q' pour annuler) : ")
        if id.lower() == 'q':
            break
        choix = input("Entrez la donnée à modifier (titre, descr, objectif, lancement, incubateur) ou 'q' : ")
        if choix.lower() == 'q':
            break
        if choix not in {"titre", "descr", "objectif", "lancement", "incubateur"}:
            print("Champ non autorisé")
            continue
        value = input("Entrez la nouvelle valeur (appuyez sur entrée s'il y en a pas) : ")
        if value == "":
            value = None

        sql = f"UPDATE Projet SET {choix}=%s WHERE id=%s"
        try:
            cur.execute(sql, (value, id))
            if cur.rowcount == 0:
                print("Aucun projet modifié.")
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

def show_projects(conn):
    queries = [
        ("Projets Artistiques", "SELECT * FROM Projet JOIN Projet_artis ON id_p = id ORDER BY id"),
        ("Projets Technologiques", "SELECT * FROM Projet JOIN Projet_techno ON id_p = id ORDER BY id"),
        ("Projets Sociaux", "SELECT * FROM Projet JOIN Projet_social ON id_p = id ORDER BY id")
    ]
    cur = conn.cursor()
    for title, sql in queries:
        try:
            cur.execute(sql)
            print(f"-----{title}----")
            raw = cur.fetchone()
            while raw:
                print(f"ID : {raw[0]}, Titre : {raw[1]}, Description : {raw[2]}, Objectif : {raw[3]}, Date de lancement : {raw[4]}, Incubateur : {raw[5]}")
                raw = cur.fetchone()
            print("-----------------------")
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
    cur.close()

def delete_project(conn):
    cur = conn.cursor()
    while True:
        id = input("Entrez l'id du projet à supprimer (ou 'q' pour annuler) : ")
        if id.lower() == 'q':
            break

        sql = "DELETE FROM Projet WHERE id=%s"
        try:
            cur.execute(sql, (id,))
            if cur.rowcount == 0:
                print("Aucun projet supprimé.")
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