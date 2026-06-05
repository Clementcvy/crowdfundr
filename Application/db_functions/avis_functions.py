import psycopg2
from datetime import datetime

def show_avis(conn, user):
    cur = conn.cursor()
    sql = "SELECT p.id, p.titre, a.note, a.texte FROM Avis a" \
          " JOIN Projet p ON a.projet = p.id" \
          " WHERE a.contributeur = %s"
    try:
        cur.execute(sql, (user,))
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
        return False
    
    raw = cur.fetchall()
    if not raw:
        print("Aucun avis trouvé pour cet utilisateur.")
        cur.close()
        return False
    
    print("-----Avis----")
    for row in raw:
        print(f"ID Projet: {row[0]}, Titre Projet : {row[1]}, Note : {row[2]},\nAvis : {row[3]}")
    print("-----------------------")
    cur.close()
    return True

def delete_avis(conn, user=None):
    if user is None:
        user = input("Entrez l'id de l'utilisateur : ")
    
    if not show_avis(conn, user):
        return

    while True:
        projet = input("Entrez l'id du projet pour lequel supprimer l'avis (ou 'q' pour annuler) : ")
        if projet.lower() == 'q':
            return
        
        cur = conn.cursor()
        sql = "DELETE FROM Avis WHERE contributeur=%s AND projet=%s"
        try:
            cur.execute(sql, (user, projet))
            if cur.rowcount == 0:
                print("ID projet incorrect. Veuillez réessayer.")
                conn.rollback()
            else:
                conn.commit()
                print("Opération réussie")
                cur.close()
                break
        except psycopg2.Error as e:
            print("Message système :", e)
            conn.rollback()
            cur.close()
            break

def insert_avis(conn, user):
    cur = conn.cursor()
    sql = """SELECT DISTINCT p.id, p.titre FROM Projet p
             JOIN Contribution co ON p.id = co.projet
             LEFT JOIN Avis a ON p.id = a.projet AND co.contributeur = a.contributeur
             WHERE a.projet IS NULL AND co.contributeur = %s;"""
    cur.execute(sql, (user,))
    
    rows = cur.fetchall()
    if not rows:
        print("Aucun projet disponible pour laisser un avis.")
        cur.close()
        return

    print("-----Projets auxquels vous avez contribué sans laisser d'avis----")
    for row in rows:
        print(f"ID : {row[0]}, Titre : {row[1]}")
    print("-----------------------")

    while True:
        projet = input("Entrez l'ID du projet (ou 'q' pour annuler) : ")
        if projet.lower() == 'q':
            cur.close()
            return
        
        if any(str(row[0]) == projet for row in rows):
            break
        print("ID invalide.")

    date_a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = 0
    while note not in [1, 2, 3, 4, 5]:
        try:
            note = int(input("Entrez la note (1-5) : "))
        except ValueError:
            continue
    texte = input("Entrez le commentaire : ")

    sql = "INSERT INTO Avis (projet, contributeur, date_a, note, texte) VALUES(%s,%s,%s,%s,%s)"
    try:
        cur.execute(sql, (projet, user, date_a, note, texte))
        conn.commit()
        print("Opération réussie")
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
    cur.close()

def update_avis(conn, user):
    cur = conn.cursor()
    sql = """SELECT DISTINCT p.id, p.titre, a.date_a, a.note, a.texte 
             FROM Projet p
             JOIN Avis a ON p.id = a.projet
             WHERE a.contributeur = %s;"""
    cur.execute(sql, (user,))
    
    rows = cur.fetchall()
    if not rows:
        print("Aucun avis trouvé à modifier.")
        cur.close()
        return

    print("-----Vos avis actuels----")
    for row in rows:
        print(f"ID : {row[0]}, Titre : {row[1]}, Note : {row[3]}, Commentaire : {row[4]}")
    
    while True:
        projet = input("Entrez l'ID du projet de l'avis à modifier (ou 'q' pour annuler) : ")
        if projet.lower() == 'q':
            cur.close()
            return
        
        if any(str(row[0]) == projet for row in rows):
            break
        print("ID invalide.")

    note = 0
    while note not in [1, 2, 3, 4, 5]:
        try:
            note = int(input("Nouvelle note (1-5) : "))
        except ValueError:
            continue
    com = input("Nouveau commentaire : ")
    date_a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = "UPDATE Avis SET note=%s, texte=%s, date_a=%s WHERE projet=%s AND contributeur=%s"
    try:
        cur.execute(sql, (note, com, date_a, projet, user))
        conn.commit()
        print("Opération réussie")
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
    cur.close()