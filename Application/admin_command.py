import psycopg2
from psycopg2 import sql
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Commandes utilisateur

#Fonction de mise à jour
def _update_user(conn, pseudo: str, col: str, val: str):
    # On prépare la requête de manière sécurisée
    # sql.Identifier(col) gère le nom de la colonne (sans guillemets simples)
    # sql.Placeholder() ou %s gère la valeur (avec guillemets simples automatiques)
    query = sql.SQL("UPDATE Contributeur SET {column} = %s WHERE pseudo = %s").format(column = sql.Identifier(col))
    curs = conn.cursor()
    try:
        curs.execute(query, (val, pseudo))
        conn.commit() 
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        conn.rollback()
        return False
    finally:
        curs.close()
    return True

#Interface admin
def update_user(conn):
    pseudo = ""
    while True:
        clear()
        print("Entrez le pseudo de l'utilisateur à modifier (\q pour quitter): ",end="")
        pseudo = input()
        if(pseudo == "\q"): return True
        pseudo_querry = "SELECT pseudo FROM Contributeur WHERE pseudo=%s;"
        try:
            curs = conn.cursor()
            curs.execute(pseudo_querry,(pseudo,))
        except:
            return False
        if curs.fetchall():
            curs.close()
            clear()
            print("Voulez vous modifier l'utilisateur: " + pseudo + "? (o/n)")
            validation = input()
            if validation == "o":
                att=""
                while(att not in ["1","2","3"]):
                    clear()
                    print("Quel attribut voulez vous modifier?\n1) Nom\n2) Date de naissance\n3) Adresse mail\n Entrée (\q retour): ",end="")
                    att = input()
                    match att:
                        case "1":
                            col = "nom"
                        case "2":
                            col = "naissance"
                        case "3":
                            col = "mail"
                        case "\q":
                            break
                        case _:
                            print("Entrée invalide.")
                            input()
                if(att!="\q"):
                    clear()
                    print("Entrez la nouvelle valeur de "+col+": ",end="")
                    edit = input()
                    _update_user(conn,pseudo,col,edit)
                    clear()
                    print("Modification effectuée avec succès!")
                    input()
                    return True
        else:
            print("L'utilisateur que vous souhaitez modifier n'existe pas dans la base de donnée.")
            input()
    

#Commandes projet

#Fonction de mise à jour
def _update_project(conn, titre: str, lancement: str, col: str, val: str):
    query = sql.SQL("UPDATE Projet SET {column} = %s WHERE titre = %s AND lancement = %s").format(column = sql.Identifier(col))
    curs = conn.cursor()
    try:
        curs.execute(query, (val, titre, lancement))
        conn.commit() 
        return True
    except Exception as e:
        print(f"Erreur Update Projet: {e}")
        conn.rollback() 
        return False
    finally:
        curs.close()

def update_project(conn):
    titre = ""
    while True:
        clear()
        print("Entrez le titre du projet à modifier (\q pour quitter): ",end="")
        titre = input()
        if(titre == "\q"): return True
        titre_querry = "SELECT titre,lancement FROM Projet WHERE titre = %s;"
        try:
            curs = conn.cursor()
            curs.execute(titre_querry,(titre,))
        except:
            print("test")
            return False
        projets=curs.fetchall()
        if projets:
            curs.close()
            clear()
            date = projets[0][1]
            if(len(projets)>1):
                id=""
                while(not (id.isdigit() and int(id)<=len(projets))):
                    clear()
                    for i in range(len(projets)):
                        print(str(i+1)+") "+titre+" - "+str(projets[i][1]))
                    print("Plusieurs projets correspondent à l'entrée\n Entrez le projet que vous souhaitez modifie: ",end="")
                    id = input()
                    if id.isdigit() and int(id)<=len(projets):
                        date = projets[int(id)-1][1]
                    else:
                        id=""
                        print("Entrée invalide.")
                        input()
            print("Voulez vous modifier le projet: " + titre + " ("+ str(date) +")? (o/n)")
            validation = input()
            if validation == "o":
                att=""
                while(att not in ["1","2","3"]):
                    clear()
                    print("Quel attribut voulez vous modifier?\n1) Description\n2) Objectif\n3) Incubateur\n Entrée (\q retour): ",end="")
                    att = input()
                    match att:
                        case "1":
                            col = "descr"
                        case "2":
                            col = "objectif"
                        case "3":
                            col = "incubateur"
                        case "\q":
                            break
                        case _:
                            print("Entrée invalide.")
                            input()
                clear()
                print("Entrez la nouvelle valeur de "+col+": ",end="")
                edit = input()
                _update_project(conn,titre,date,col,edit)
                clear()
                print("Modification effectuée avec succès!")
                input()
                return True
        else:
            print("Le projet que vous souhaitez modifier n'existe pas dans la base de donnée.")
            input()