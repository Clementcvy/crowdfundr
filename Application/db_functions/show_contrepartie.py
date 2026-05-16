import psycopg2


def show_contreparties(conn, contributeur):
    sql = "SELECT id_c, poids, frais, transporteur FROM Contrepartie_physique CP JOIN Contribution C ON CP.id_c=C.id WHERE C.contributeur=%s"

    cur = conn.cursor()
    try:
        cur.execute(sql, (contributeur,))
    except psycopg2.Error as e:
        print("Message système :", e)

    raw = cur.fetchone()
    print("-----Contrepartie Physique-----")
    while raw:
        print(
            f"ID_c: {raw[0]}, Poids : {raw[1]}, Frais de livraison : {raw[2]}, Transporteur: {raw[3]}"
        )
        raw = cur.fetchone()
    print("-----------------------")

    sql = "SELECT id_c, format, taille FROM Contrepartie_numerique CN JOIN Contribution C ON CN.id_c=C.id WHERE C.contributeur=%s"
    try:
        cur.execute(sql, (contributeur,))
    except psycopg2.Error as e:
        print("Message système :", e)

    raw = cur.fetchone()
    print("-----Contrepartie Numérique-----")
    while raw:
        print(f"ID_c: {raw[0]}, Format : {raw[1]}, Taille : {raw[2]}")
        raw = cur.fetchone()
    print("-----------------------")
