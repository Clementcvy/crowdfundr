import database_connect as dbc
import psycopg2
from db_functions.db_selects import select1, select2, select3
from db_functions.show_contribution import show_contributions
from db_functions.insert_contrepartie import insert_contrepartie
from db_functions.delete_contrepartie import delete_contrepartie
from db_functions.print_personne import print_personne
from db_functions.insert_contribution import insert_contribution
from db_functions.update_contribution import update_contribution
from db_functions.delete_contribution import delete_contribution
from db_functions.show_contrepartie import show_contreparties
from db_functions.update_contrepartie import update_contrepartie
from db_functions.show_projects import show_projects
from db_functions.show_users import show_users
from db_functions.insert_user import insert_user
from db_functions.update_user import update_user
import time


def pause():
    input("Appuyez sur entrée pour passer à la suite : ")


def mainMenu(conn):
    print("1 - Connexion utilisateur")
    print("2 - Admin")
    print("0 - Quitter")
    choice = int(input("--> "))
    match choice:
        case 1:
            contributeur = login(conn)
            userMenu(conn, contributeur)
            return True
        case 2:
            adminMenu(conn)
            return True
        case _:
            return False


def userMenu(conn, contributeur):
    print("")
    print("1 - Afficher mes informations")
    print("2 - Contrepartie")
    print("3 - Contribution")
    choice = int(input("--> "))
    match choice:
        case 1:
            print_personne(conn, contributeur)
            pause()
        case 2:
            show_contreparties(conn, contributeur)
            # Contrepartie
            print("1 - UPDATE")
            print("2 - INSERT")
            print("3 - DELETE")
            choice = input("-> ")
            print("-----------")
            match int(choice):
                case 1:
                    update_contrepartie(conn, contributeur)
                    pause()
                case 2:
                    insert_contrepartie(conn, contributeur)
                    pause()
                case 3:
                    delete_contrepartie(conn, contributeur)
                    pause()
                case _:
                    print("Choix inconnu.")
                    time.sleep(0.5)
            print("-----------")
        case 3:
            # Contribution
            show_contributions(conn, contributeur)
            print("1 - UPDATE")
            print("2 - INSERT")
            print("3 - DELETE")
            choice = input("-> ")
            match int(choice):
                case 1:
                    update_contribution(conn, contributeur)
                    pause()
                case 2:
                    insert_contribution(conn, contributeur)
                    pause()
                case 3:
                    delete_contribution(conn, contributeur)
                    pause()
                case _:
                    print("Choix inconnu.")
                    time.sleep(0.5)
            print("-----------")
        case _:
            print("Choix non connu.")
            time.sleep(0.5)


def adminMenu(conn):
    print("")
    print("1 - Gérer les utilisateurs")
    print("2 - Gérer les projets")
    print("3 - SELECT")
    print("4 - Afficher tous les projets")
    print("5 - Afficher tous les utilisateurs")
    choice = int(input("--> "))
    match choice:
        case 1:
            print("1 - UPDATE")
            print("2 - INSERT")
            print("3 - DELETE")
            choice = input("-> ")
            match int(choice):
                case 1:
                    update_user(conn)
                    pause()
                case 2:
                    insert_user(conn)
                    pause()
                case 3:
                    pass
                case _:
                    pass
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
            show_projects(conn)
            pause()
        case 5:
            show_users(conn)
            pause()
        case _:
            print("Choix non connu.")
            time.sleep(0.5)


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

        sql = "SELECT id FROM Contributeur WHERE id=%s"
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

    return id


if __name__ == "__main__":
    conn = dbc.connectDatabase()
    try:
        noQuit = True
        while noQuit:
            noQuit = mainMenu(conn)
    except KeyboardInterrupt as k:
        print("")
        print("Exiting...")
    finally:
        dbc.exitDatabase(conn)
