import psycopg2
from db_functions.member_functions import show_members
from db_functions.project_functions import show_projects

def show_membership(conn, projet):
    sql = """SELECT M.id, M.nom, M.naissance, M.prenom, M.pays, MP.role_m
    FROM MembreProjet MP
    JOIN Membre M ON M.id=MP.membre
    WHERE MP.projet=%s
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, (projet,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        cur.close()
        return

    raw = cur.fetchone()
    print(f"-----Membre(s) du projet {projet}-----")
    while raw:
        print(f"ID : {raw[0]}, Nom : {raw[1]}, Date de naissance : {raw[2]}, Prenom : {raw[3]}, Pays : {raw[4]}, Role : {raw[5]}")
        raw = cur.fetchone()
    print("-----------------------")
    cur.close()


def delete_membership(conn):
    cur = conn.cursor()
    while True:
        projet = input("Entrez l'id du projet que vous voulez traiter (ou 'q' pour annuler) : ")
        if projet.lower() == "q":
            break
        show_membership(conn, projet)
        membre = input("Entrez l'ID du membre a retirer (ou 'q' pour annuler) : ")
        if membre.lower() == "q":
            break

        sql = "DELETE FROM MembreProjet WHERE projet=%s AND membre=%s"
        try:
            cur.execute(sql, (projet, membre))
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

def insert_membership(conn):
    cur = conn.cursor()
    while True:
        projet = input("Entrez l'id du projet (ou 'q' pour annuler) : ")
        if projet.lower() == "q":
            break
        
        sql = """SELECT DISTINCT M.id, M.nom, M.naissance, M.prenom, M.pays FROM Membre M
        LEFT JOIN MembreProjet MP ON M.id=MP.membre
        AND MP.projet = %s
        WHERE MP.membre IS NULL
        ORDER BY id;
        """
        try:
            cur.execute(sql, (projet,))
            raw = cur.fetchone()
            print("-----Membres ne faisant pas partie du projet----")
            while raw:
                print(f"ID : {raw[0]}, Nom : {raw[1]}, Date de naissance : {raw[2]}, Prenom : {raw[3]}, Pays : {raw[4]}")
                raw = cur.fetchone()
            print("-----------------------")
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            cur.close()
            return

        membre = input("Entrez l'ID du membre que vous souhaitez ajouter (ou 'q' pour annuler) : ")
        if membre.lower() == "q":
            break
        role = input("Entrez le role a attribuer au membre ('chef de projet', 'développeur', 'designer', 'community manager') : ")
        if role not in ['chef de projet', 'développeur', 'designer', 'community manager']:
            print("Role invalide")
            continue
        try:
            sql = "INSERT INTO MembreProjet (projet, membre, role_m) VALUES (%s, %s, %s)"
            cur.execute(sql, (projet, membre, role))
            conn.commit()
            print("Opération réussie")
            break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            continue
    cur.close()