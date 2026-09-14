import os
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def run_mongo_script(filename):
    os.system(f'mongosh "{SCRIPT_DIR / filename}"')


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    input("\nAppuyez sur entrée pour continuer...")


if __name__ == "__main__":
    try:
        while True:
            clear()
            print("Bienvenue sur l'application Projet NF18 MongoDB")
            print("Choix :")
            print("1 - Insérer un projet")
            print("2 - Supprimer un avis")
            print("3 - Mettre à jour un avis")
            print("4 - Sélectionner un membre")
            print("5 - Selects")
            print("0 - Sortir")
            choix = int(input("-> "))

            if choix == 1:  # Insérer un projets
                run_mongo_script("01_insertion_projets.js")
            elif choix == 2:
                run_mongo_script("02_suppression_avis.js")
            elif choix == 3:
                run_mongo_script("03_mise_a_jour_avis.js")
            elif choix == 4:
                run_mongo_script("04_selection_membres.js")
            elif choix == 5:
                clear()
                print("Choix :")
                print(
                    "1 - Quels projets artistiques font intervenir à la fois deux membres et ont dépassé leur objectif financier ?"
                )
                print(
                    "2 - Quelle est la moyenne des notes des projets sociaux qui sont soutenus par une ONG de votre choix, en ne prenant en compte que les utilisateurs ayant apporté une contribution supérieure à un montant de votre choix sur ces projets ?"
                )
                print(
                    "3 - Pour chaque projet accompagné par un incubateur, combien d'utilisateurs distincts ont réclamé au moins une contrepartie physique expédiée via le transporteur de votre choix lors de leurs contributions ?"
                )
                reponse = int(input("-> "))
                if reponse == 1:
                    run_mongo_script("05_recherche_projets_artisanaux_finances.js")
                elif reponse == 2:
                    run_mongo_script("06_recherche_moyenne_avis_ong.js")
                elif reponse == 3:
                    run_mongo_script("07_recherche_contributeurs_chronopost.js")
            elif choix == 0:
                break
            pause()
    except KeyboardInterrupt as e:
        print("Sortie de l'app...")
        exit(0)
