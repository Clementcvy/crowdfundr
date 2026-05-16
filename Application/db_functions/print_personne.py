#!/usr/bin/python3

# http://initd.org/psycopg/docs/usage.html

import psycopg2


def print_personne(conn, id):
    # Open a cursor to send SQL commands
    cur = conn.cursor()

    # Execute a SQL SELECT command
    sql = "SELECT * FROM Contributeur WHERE id = %s"
    try:
        cur.execute(sql, (id,))

        # Fetch data line by line
        raw = cur.fetchone()
        print("Voici vos informations")
        while raw:
            print(f"ID : {raw[0]}")
            print(f"Nom : {raw[1]}")
            print(f"Date de naissance : {raw[2]}")
            print(f"Pseudo : {raw[3]}")
            print(f"Mail : {raw[4]}")
            raw = cur.fetchone()
    except psycopg2.Error as e:
        print("Message système :", e)
        conn.rollback()
