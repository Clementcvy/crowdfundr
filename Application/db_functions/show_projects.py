import psycopg2


def show_projects(conn):
    sql = "SELECT * FROM Projet ORDER BY id"

    cur = conn.cursor()
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Projets----")
    while raw:
        print(
            f"ID : {raw[0]}, Titre : {raw[1]}, Description : {raw[2]}, Objectif : {raw[3]},"
        )
        print(f"Date de lancement : {raw[4]}, Incubateur : {raw[5]}")
        raw = cur.fetchone()
    print("-----------------------")
