import psycopg2

def show_contributions(conn, id):
    sql = "SELECT Contribution.id, date_c, montant, projet FROM Contribution JOIN Contributeur ON Contribution.contributeur = Contributeur.id WHERE Contributeur.id = %s" % (id)

    cur = conn.cursor()
    try :
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)

      # Fetch data line by line
    raw = cur.fetchone()
    print("-----Contributions-----")
    while raw:
        print(f"id: {raw[0]}, date: {raw[1]}, montant: {raw[2]}, projet: {raw[3]}")
        raw = cur.fetchone()
    print("-----------------------")