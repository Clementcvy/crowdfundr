#!/usr/bin/python3

import psycopg2

def insert_contrepartie(conn):

    # Open a cursor to send SQL commands
    cur = conn.cursor()

    choix = input("1 pour une contrepartie physique, 2 pour un contrepartie numérique : ")

    id_c = input("Choisissez l'id de le contribution dont vous voulez inserer une contrepartie : ")

    sql = "INSERT INTO Contrepartie VALUES (%s)" % (id_c)
    try :
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)

    if int(choix) == 1:
        format = input("Entrez le format : ")
        taille = input("Entrez la taille : ")
        sql = "INSERT INTO Contrepartie_numerique (id_c, format, taille) VALUES ('%s', '%s', %s)" % (id_c, format, taille)
    elif int(choix) == 2:
        poids = input("Entrez le poids : ")
        frais = input("Entrez les frais : ")
        transporteur = input("Entrez le transporteur : ")
        sql = "INSERT INTO Contrepartie_physique (id_c, poids, frais, transporteur) VALUES (%s, %s, %s, '%s')" % (id_c, poids, frais, transporteur)

    try :
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)

    conn.commit()
