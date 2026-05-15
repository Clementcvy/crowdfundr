import database_connect as dbc
import psycopg2
from db_functions.db_selects import select1, select2, select3
from db_functions.show_contribution import show_contributions
from db_functions.insert_contrepartie import insert_contrepartie
from db_functions.delete_contrepartie import delete_contrepartie
from db_functions.print_personne import print_personne
import time


def Pause():
    input("Appuyez sur entrée pour passer à la suite : ")


def printMenu(id, conn):
    print("----------------------")
    if id == "admin":
        print("Vous êtes Admin")
        print("")
        print("1 - Gérer les utilisateurs")
        print("2 - Gérer les projets")
        print("3 - SELECT")
        print("4 - Afficher toutes les tables")
    else:
        # Afficher ID utilisateur ?
        print("")
        print("1 - Afficher mes informations")
        print("2 - Contrepartie")
        print("3 - Contribution")

    return input("Quel est votre choix ? : ")


def handleMenu(rep, id, conn):
    print("")
    if id == "admin":
        match int(rep):
            case 1:
                print("1 - UPDATE")
                print("2 - INSERT")
                print("3 - DELETE")
                choice = input("-> ")
                # Appeler les fonctions correspondantes
            case 2:
                print("1 - UPDATE")
                print("2 - INSERT")
                print("3 - DELETE")
                choice = input("-> ")
                # Appeler les fonctions correspondantes
            case 3:
                print(
                    "1 - Quels projets artistiques font intervenir à la fois Hideo Kojima et Yoji Shinkawa (membres d'équipe) et ont dépassé leur objectif financier (somme des contributions > objectif) ?"
                )
                print(
                    "2 - Quelle est la moyenne des notes des projets sociaux qui sont soutenus par l'ONG nommée Amnesty International, en ne prenant en compte que les utilisateurs ayant apporté une contribution supérieure à 50 euros sur ces projets ?"
                )
                print(
                    "3 - Pour chaque projet accompagné par un incubateur, combien d'utilisateurs distincts ont réclamé au moins une contrepartie physique expédiée via le transporteur  Chronopost lors de leurs contributions ?"
                )
                choice = input("-> ")
                print("-----------")
                match int(choice):
                    case 1:
                        select1(conn)
                    case 2:
                        select2(conn)
                    case 3:
                        select3(conn)
                    case _:
                        print("Choix non connu.")
                        time.sleep(0.5)
                print("-----------")

            case 4:
                # Appeler fonction corres
                print("")
            case _:
                print("Choix non connu.")
                time.sleep(0.5)
    else:
        match int(rep):
            case 1:
                print_personne(conn, id)
                Pause()
            case 2:
                show_contributions(conn, id)
                # Contrepartie
                print("1 - UPDATE")
                print("2 - INSERT")
                print("3 - DELETE")
                choice = input("-> ")
                print("-----------")
                match int(choice):
                    case 1:
                        print("A FAIRE")
                    case 2:
                        insert_contrepartie(conn)
                    case 3:
                        delete_contrepartie(conn)
                    case _:
                        print("Choix inconnu.")
                        time.sleep(0.5)
                print("-----------")

            case 3:
                # Contribution
                print("1 - UPDATE")
                print("2 - INSERT")
                print("3 - DELETE")
                choice = input("-> ")
            case _:
                print("Choix non connu.")
                time.sleep(0.5)

    time.sleep(0)
    return


def login(conn):

    cur = conn.cursor()

    # affichage des contributeurs
    sql = "SELECT id, nom, pseudo FROM Contributeur"
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)

    raw = cur.fetchone()
    print("-----Contributeurs-----")
    while raw:
        print(f"id: {raw[0]}, nom: {raw[1]}, pseudo: {raw[2]}")
        raw = cur.fetchone()
    print("-----------------")

    access_granted = False
    while not access_granted:
        print("")
        id = input("ID : ")

        sql = "SELECT id, nom, pseudo FROM Contributeur WHERE id=%s"
        try:
            # utilisation d'une requête paramétrée
            cur.execute(sql, (id,))
        except psycopg2.Error as e:
            print("Message système :", e)

        raw = cur.fetchone()
        if not raw:
            print("[ERREUR] L'utilisateur demandé n'existe pas.")
        else:
            access_granted = True

    member = {"id": id, "nom": raw[1], "pseudo": raw[2]}
    return member


if __name__ == "__main__":
    conn = dbc.connectDatabase()
    try:
        while True:
            member = login(conn)
            print("")
            print("Bienvenue ", member["pseudo"])
            rep = printMenu(member["id"], conn)
            handleMenu(rep, member["id"], conn)
    except KeyboardInterrupt as k:
        print("")
        print("Exiting...")
        dbc.exitDatabase(conn)
