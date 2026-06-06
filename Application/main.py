import psycopg2
from db_functions.db_selects import select1, select2, select3
from db_functions.print_personne import print_personne
from db_functions.project_functions import (
    insert_project,
    update_project,
    show_projects,
    delete_project,
)
from db_functions.contrepartie_functions import (
    update_contrepartie,
    show_contreparties,
    insert_contrepartie,
    delete_contrepartie,
    show_transporteurs,
)
from db_functions.contribution_functions import (
    update_contribution,
    show_contributions,
    insert_contribution,
    delete_contribution,
)
from db_functions.user_functions import (
    delete_user,
    insert_user,
    show_users,
    update_user,
)
from db_functions.transporteur_fonctions import (
    delete_transporteur,
    insert_transporteur,
    update_transporteur,
)
from db_functions.ong_functions import (
    show_ong,
    insert_ong,
    update_ong,
    delete_ong,
)
from db_functions.projetsocial_ong import (
    show_social_ong,
    insert_social_ong,
    # update_social_ong,
    delete_social_ong,
)
from db_functions.incubateur_functions import (
    show_incubateur,
    insert_incubateur,
    delete_incubateur,
    update_incubateur,
)
from db_functions.avis_functions import delete_avis, insert_avis, show_avis, update_avis
from db_functions.member_functions import delete_member, insert_member, show_members, update_member
import time
import os
import database_connect as dbc


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input("\nAppuyez sur entrée pour continuer...")


def mainMenu(conn):
    while True:
        clear()
        print("1 - Connexion utilisateur")
        print("2 - Admin")
        print("0 - Quitter")
        choice = input("--> ")
        if choice == "1":
            contributeur = login(conn)
            if contributeur:
                userMenu(conn, contributeur)
        elif choice == "2":
            adminMenu(conn)
        elif choice == "0":
            return False
        else:
            print("Choix invalide.")
            time.sleep(0.5)


def userMenu(conn, contributeur):
    while True:
        clear()
        print("1 - Afficher mes informations")
        print("2 - Gérer les contreparties")
        print("3 - Faire une contribution")
        print("4 - Gérer les avis")
        print("0 - Retour")
        choice = input("--> ")
        if choice == "1":
            clear()
            print_personne(conn, contributeur)
            pause()
        elif choice == "2":
            while True:
                clear()
                show_contreparties(conn, contributeur)
                print("1 - INSERT")
                print("2 - DELETE")
                print("0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    insert_contrepartie(conn, contributeur)
                    pause()
                elif sub == "2":
                    delete_contrepartie(conn, contributeur)
                    pause()
                elif sub == "0":
                    break
        elif choice == "3":
            clear()
            show_contributions(conn, contributeur)
            insert_contribution(conn, contributeur)
            pause()
        elif choice == "4":
            while True:
                clear()
                print("1 - Laisser un avis")
                print("2 - Modifier un avis")
                print("3 - Supprimer un avis")
                print("0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    insert_avis(conn, contributeur)
                    pause()
                elif sub == "2":
                    update_avis(conn, contributeur)
                    pause()
                elif sub == "3":
                    delete_avis(conn, contributeur)
                    pause()
                elif sub == "0":
                    break
        elif choice == "0":
            break


def adminMenu(conn):
    while True:
        clear()
        print("1 - Gérer les utilisateurs")
        print("2 - Gérer les membres")
        print("3 - Gérer les projets")
        print("4 - SELECT")
        print("5 - Afficher tous les projets")
        print("6 - Afficher tous les utilisateurs")
        print("7 - Gérer les contributions")
        print("8 - Gérer les contreparties")
        print("9 - Gérer les transporteurs")
        print("10 - Gérer les ONGs")
        print("11 - Gérer les liens Projet social - ONG")
        print("12 - Gérer les incubateurs")
        print("13 - Supprimer l'avis d'un utilisateur")
        print("0 - Retour")
        choice = input("--> ")
        if choice == "0":
            break
        elif choice == "1":
            while True:
                clear()
                show_users(conn)
                print("1 - UPDATE | 2 - INSERT | 3 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_user(conn)
                    pause()
                elif sub == "2":
                    insert_user(conn)
                    pause()
                elif sub == "3":
                    delete_user(conn)
                    pause()
                elif sub == "0":
                    break
        
        elif choice == "2":
            while True:
                clear()
                show_members(conn)
                print("1 - UPDATE | 2 - INSERT | 3 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_member(conn)
                    pause()
                elif sub == "2":
                    insert_member(conn)
                    pause()
                elif sub == "3":
                    delete_member(conn)
                    pause()
                elif sub == "0":
                    break

        elif choice == "3":
            while True:
                clear()
                show_projects(conn)
                print("1 - UPDATE | 2 - INSERT | 3 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_project(conn)
                    pause()
                elif sub == "2":
                    insert_project(conn)
                    pause()
                elif sub == "3":
                    delete_project(conn)
                    pause()
                elif sub == "0":
                    break
        elif choice == "4":
            while True:
                clear()
                print(
                    "1 - Quels projets artistiques font intervenir à la fois deux membres et ont dépassé leur objectif financier ?"
                )
                print(
                    "2 - Quelle est la moyenne des notes des projets sociaux qui sont soutenus par une ONG de votre choix, en ne prenant en compte que les utilisateurs ayant apporté une contribution supérieure à un montant de votre choix sur ces projets ?"
                )
                print(
                    "3 - Pour chaque projet accompagné par un incubateur, combien d'utilisateurs distincts ont réclamé au moins une contrepartie physique expédiée via le transporteur de votre choix lors de leurs contributions ?"
                )
                print("0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    select1(conn)
                    pause()
                elif sub == "2":
                    select2(conn)
                    pause()
                elif sub == "3":
                    select3(conn)
                    pause()
                elif sub == "0":
                    break
        elif choice == "5":
            clear()
            show_projects(conn)
            pause()
        elif choice == "6":
            clear()
            show_users(conn)
            pause()
        elif choice == "7":
            contributeur = login(conn)
            if contributeur:
                show_contributions(conn, contributeur)
                print("1 - UPDATE | 2 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_contribution(conn, contributeur)
                    pause()
                elif sub == "2":
                    delete_contribution(conn, contributeur)
                    pause()
        elif choice == "8":
            contributeur = login(conn)
            if contributeur:
                show_contreparties(conn, contributeur)
                print("1 - UPDATE | 2 - INSERT | 3 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_contrepartie(conn, contributeur)
                    pause()
                elif sub == "2":
                    insert_contrepartie(conn, contributeur)
                    pause()
                elif sub == "3":
                    delete_contrepartie(conn, contributeur)
                    pause()
        elif choice == "9":
            while True:
                clear()
                show_transporteurs(conn)
                print("1 - UPDATE | 2 - INSERT | 3 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_transporteur(conn)
                    pause()
                elif sub == "2":
                    insert_transporteur(conn)
                    pause()
                elif sub == "3":
                    delete_transporteur(conn)
                    pause()
                elif sub == "0":
                    break
        elif choice == "10":
            while True:
                clear()
                show_ong(conn)
                print("1 - UPDATE | 2 - INSERT | 3 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_ong(conn)
                    pause()
                elif sub == "2":
                    insert_ong(conn)
                    pause()
                elif sub == "3":
                    delete_ong(conn)
                    pause()
                elif sub == "0":
                    break
        elif choice == "11":
            while True:
                clear()
                show_social_ong(conn)
                print("1 - INSERT | 2 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    insert_social_ong(conn)
                    pause()
                elif sub == "2":
                    delete_social_ong(conn)
                    pause()
                elif sub == "0":
                    break
        elif choice == "12":
            while True:
                clear()
                show_incubateur(conn)
                print("1 - UPDATE | 2 - INSERT | 3 - DELETE | 0 - Retour")
                sub = input("-> ")
                if sub == "1":
                    update_incubateur(conn)
                    pause()
                elif sub == "2":
                    insert_incubateur(conn)
                    pause()
                elif sub == "3":
                    delete_incubateur(conn)
                    pause()
                elif sub == "0":
                    break
        elif choice == "13":
            clear()
            delete_avis(conn)
            pause()


def login(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, nom, pseudo FROM Contributeur")
    raw = cur.fetchall()
    print("-----Contributeurs-----")
    for r in raw:
        print(f"id: {r[0]}, nom: {r[1]}, pseudo: {r[2]}")
    print("-----------------")

    while True:
        id_user = input("ID (ou 'q' pour annuler) : ")
        if id_user == "q":
            return None
        cur.execute("SELECT id FROM Contributeur WHERE id=%s", (id_user,))
        if cur.fetchone():
            return id_user
        print("[ERREUR] Inexistant.")


if __name__ == "__main__":
    conn = dbc.connectDatabase()
    try:
        while mainMenu(conn):
            pass
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        dbc.exitDatabase(conn)
