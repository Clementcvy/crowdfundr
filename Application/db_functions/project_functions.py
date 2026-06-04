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

def insert_project(conn):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    titre = input("Entrez le titre du projet : ")
    descr = input("Entrez la description du projet : ")
    objectif = input("Entrez l'objectif du projet : ")
    lancement = input("Entrez la date de lancement du projet : ")
    show_incubateurs(conn)
    incubateur = input(
        "Entrez l'incubateur du projet (appuyez sur entrée s'il y en a pas): "
    )
    if incubateur == "":
        incubateur = None

    type_projet = input("Entrez le type du projet (Projet social : 1, Projet techno : 2, Projet artis : 3) : ")

    if int(type_projet) not in (1, 2, 3):
        print("Message système : Option non possible.")
        return

    match int(type_projet):
        case 1: #Projet social
            print("Vous avez sélectionné 'Projet Social' :")
            region = input("Entrez la région : ")
        case 2: #Projet Techno
            print("Vous avez sélectionné 'Projet Technologique' :")
            innovation = input("Entrez l'innovation : ")
        case 3: #Projet Artis
            print("Vous avez sélectionné 'Projet Artistique' :")
            medium = input("Entrez le médium : ")

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

    match int(type_projet):
        case 1: #Projet social
            sql = "INSERT INTO Projet_social (id_p, region) VALUES (%s, %s)"
            try:
                cur.execute(sql, (id, region))
            except psycopg2.Error as e:
                print("Message système :", e)
                conn.rollback()
                return

        case 2: #Projet Techno
            sql = "INSERT INTO Projet_techno (id_p, innovation) VALUES (%s, %s)"
            try:
                cur.execute(sql, (id, innovation))
            except psycopg2.Error as e:
                print("Message système :", e)
                conn.rollback()
                return
        case 3: #Projet Artis
            sql = "INSERT INTO Projet_artis (id_p, medium) VALUES (%s, %s)"
            try:
                cur.execute(sql, (id, medium))
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

    #PROJETS ARTISTIQUES
    sql = "SELECT * FROM Projet JOIN Projet_artis ON id_p = id ORDER BY id"

    cur = conn.cursor()
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Projets Artistiques----")
    while raw:
        print(
            f"ID : {raw[0]}, Titre : {raw[1]}, Description : {raw[2]}, Objectif : {raw[3]}, Date de lancement : {raw[4]}, Incubateur : {raw[5]}"
        )
        raw = cur.fetchone()
    print("-----------------------")

    # PROJETS TECHNOLOGIQUES
    sql = "SELECT * FROM Projet JOIN Projet_techno ON id_p = id ORDER BY id"


    cur = conn.cursor()
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Projets Technologiques----")
    while raw:
        print(
            f"ID : {raw[0]}, Titre : {raw[1]}, Description : {raw[2]}, Objectif : {raw[3]}, Date de lancement : {raw[4]}, Incubateur : {raw[5]}"
        )
        raw = cur.fetchone()
    print("-----------------------")

    # PROJETS SOCIAL
    sql = "SELECT * FROM Projet JOIN Projet_social ON id_p = id ORDER BY id "

    cur = conn.cursor()
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Projets Sociaux----")
    while raw:
        print(
            f"ID : {raw[0]}, Titre : {raw[1]}, Description : {raw[2]}, Objectif : {raw[3]}, Date de lancement : {raw[4]}, Incubateur : {raw[5]}"
        )
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
