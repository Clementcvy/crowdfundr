import database_connect as dbc
from db_functions.db_selects import *
from db_functions.delete_contrepartie import *
from db_functions.delete_contribution import *
from db_functions.insert_contrepartie import *
from db_functions.insert_contribution import *
from db_functions.show_contributions import *
import time


def printMenu(id, conn):
    print("Application base SQL :")
    print("----------------------")
    if id =="admin":
        print("Vous êtes Admin")
        print("")
        print("1 - Gérer les utilisateurs")
        print("2 - Gérer les projets")
        print("3 - SELECT")
        print("4 - Afficher toutes les tables")
    else:
        #Afficher ID utilisateur ?
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
                #Appeler les fonctions correspondantes
            case 2:
                print("1 - UPDATE")
                print("2 - INSERT")
                print("3 - DELETE")
                choice = input("-> ")
                #Appeler les fonctions correspondantes
            case 3:
                print("1 - Quels projets artistiques font intervenir à la fois Hideo Kojima et Yoji Shinkawa (membres d'équipe) et ont dépassé leur objectif financier (somme des contributions > objectif) ?")
                print("2 - Quelle est la moyenne des notes des projets sociaux qui sont soutenus par l'ONG nommée Amnesty International, en ne prenant en compte que les utilisateurs ayant apporté une contribution supérieure à 50 euros sur ces projets ?")
                print("3 - Pour chaque projet accompagné par un incubateur, combien d'utilisateurs distincts ont réclamé au moins une contrepartie physique expédiée via le transporteur  Chronopost lors de leurs contributions ?")
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
                #Appeler fonction corres
                print("")
            case _:
                print("Choix non connu.")
                time.sleep(0.5)
    else:
        match int(rep):
            case 1:
                print("Affichage des informations")
            case 2:
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


    time.sleep(2)
    return




if __name__ == "__main__":
    conn = dbc.connectDatabase()
    id = input("ID : ")
    show_contributions(conn, id)
    try:
        while True:
            rep = printMenu(id, conn)
            handleMenu(rep, id, conn)
    except KeyboardInterrupt as k:
        print("")
        print("Exiting...")
        dbc.exitDatabase(conn)