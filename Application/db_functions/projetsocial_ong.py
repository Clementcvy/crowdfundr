#!/usr/bin/python3

import psycopg2

from db_functions.ong_functions import show_ong


def show_social_ong(conn):
    sql = """SELECT P.titre, P.id, O.nom, O.NEU
    FROM Projet_socialONG PO, Projet P, Projet_social PS, ONG O
    WHERE P.id=PS.id_p AND PO.projet = P.id AND PO.ONG=O.NEU
    """
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        cur.close()
        return

    raw = cur.fetchone()
    print("-------Projet et ONG-------")
    while raw:
        print(
            f"projet: (nom: {raw[0]}, id: {raw[1]}) soutenu par: (nom: {raw[2]}, NEU: {raw[3]})"
        )
        raw = cur.fetchone()
    print("-----------------------")
    cur.close()


def delete_social_ong(conn):
    cur = conn.cursor()
    while True:
        show_social_ong(conn)
        projet = input(
            "Entrez l'id du projet dont l'association est à supprimer (ou 'q' pour annuler) : "
        )
        if projet.lower() == "q":
            break
        neu = input(
            "Entrez le neu de l'ONG dont l'association est à supprimer (ou 'q' pour annuler) : "
        )
        if neu.lower() == "q":
            break

        sql = "DELETE FROM Projet_socialONG WHERE projet=%s AND ONG=%s"
        try:
            cur.execute(sql, (projet, neu))
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


def show_social_project(conn):
    sql = "SELECT P.id, P.titre, P.descr, P.objectif, P.lancement, P.incubateur, PS.region FROM Projet P JOIN Projet_social PS ON PS.id_p = P.id ORDER BY P.id"
    cur = conn.cursor()
    try:
        cur.execute(sql)
        print("-----Projet Social----")
        raw = cur.fetchone()
        while raw:
            print(
                f"ID : {raw[0]}, Titre : {raw[1]}, Description : {raw[2]}, Objectif : {raw[3]}, Date de lancement : {raw[4]}, Incubateur : {raw[5]}, region : {raw[6]}"
            )
            raw = cur.fetchone()
        print("-----------------------")
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
    cur.close()


def insert_social_ong(conn):
    cur = conn.cursor()
    while True:
        show_social_project(conn)
        projet = input("Entrez l'id du projet (ou 'q' pour annuler) : ")
        if projet.lower() == "q":
            break
        show_ong(conn)
        neu = input("Entrez le NEU de l'ONG (ou 'q' pour annuler) : ")
        if neu.lower() == "q":
            break

        try:
            sql = "INSERT INTO Projet_socialONG (projet, ONG) VALUES (%s, %s)"
            cur.execute(sql, (projet, neu))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()


# def update_social_ong(conn):
#     cur = conn.cursor()
#     while True:
#         show_social_ong(conn)
#         projet = input(
#             "Entrez l'id du projet dont les données sont à mettre à jour (ou 'q' pour annuler) : "
#         )
#         if projet.lower() == "q":
#             break
#         neu = input(
#             "Entrez le neu de l'ONG dont les données sont à mettre à jour (ou 'q' pour annuler) : "
#         )
#         if projet.lower() == "q":
#             break

#         choix = input("Entrez la donnée à modifier (projet, ONG) ou 'q' : ")
#         if choix.lower() == "q":
#             break
#         if choix not in {"projet", "ONG"}:
#             print("Champ non autorisé")
#             continue

#         value = input("Entrez la nouvelle valeur : ")

#         sql = f"UPDATE Projet_socialONG SET {choix}=%s WHERE projet=%s AND ONG=%s"
#         try:
#             cur.execute(sql, (value, projet, neu))
#             if cur.rowcount == 0:
#                 print("Aucun utilisateur modifié.")
#                 conn.rollback()
#             else:
#                 conn.commit()
#                 print("Opération réussie")
#                 break
#         except psycopg2.Error as e:
#             print("Message système :", e)
#             conn.rollback()
#             continue
#     cur.close()
