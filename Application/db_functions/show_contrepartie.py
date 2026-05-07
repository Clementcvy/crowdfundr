def show_contreparties(conn, id):
    sql = "SELECT id_c, poids, frais, transporteur FROM Contrepartie_physique cp JOIN Contrepartie c ON cp.id_c=c.id_c JOIN Contribution co ON c.id_c=id  JOIN Contributeur ct ON ct.id=co.contributeur WHERE ct.id = %s" % (id)

    cur = conn.cursor()
    try :
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)

    sql = "SELECT id_c, format, taille FROM Contrepartie_numerique WHERE id_c = %s" % (id)
    try :
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        print("Message système :", e)

      # Fetch data line by line
    raw = cur.fetchone()
    print("-----Contrepartie-----")
    while raw:
        print(f"id: {raw[0]}, date: {raw[1]}, montant: {raw[2]}, projet: {raw[3]}")
        raw = cur.fetchone()
    print("-----------------------")