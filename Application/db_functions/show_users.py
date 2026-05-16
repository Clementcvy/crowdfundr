import psycopg2


def show_users(conn):
    sql = "SELECT * FROM Contributeur ORDER BY id"

    cur = conn.cursor()
    try:
        cur.execute(sql)
    except psycopg2.Error as e:
        print("Message système :", e)
        return

    # Fetch data line by line
    raw = cur.fetchone()
    print("-----Utilisateurs----")
    while raw:
        print(f"ID : {raw[0]}, Nom : {raw[1]}, Date de naissance : {raw[2]},")
        print(f"Pseudo : {raw[3]}, Mail : {raw[4]}")
        raw = cur.fetchone()
    print("-----------------------")
