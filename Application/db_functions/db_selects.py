# Execute a SQL SELECT command
def select1(conn):
  sql = "SELECT DISTINCT pa.id_p \
  FROM Projet_artis pa  \
  JOIN Projet p ON p.id = pa.id_p\
  JOIN MembreProjet mp1 ON mp1.projet = p.id\
  JOIN Membre m1 ON m1.id = mp1.membre\
  JOIN MembreProjet mp2 ON mp2.projet = p.id\
  JOIN Membre m2 ON m2.id = mp2.membre\
  WHERE m1.nom = 'Shinkawa'\
    AND m1.prenom = 'Yoji'\
    AND m2.nom = 'Kojima'\
    AND m2.prenom = 'Hideo'\
    AND (\
        SELECT SUM(c.montant)\
        FROM Contribution c\
        WHERE c.projet = p.id\
    ) >= p.objectif\
  "
  cur = conn.cursor()
  try:
    cur.execute(sql)
  except Error as e:
    print("[LOGS] Error request 1")
    return False

  # Fetch data line by line
  raw = cur.fetchone()
  while raw:
      print (raw[0])
      raw = cur.fetchone()
      
  return True

def select2(conn):
    sql = "select AVG(note) from Avis\
    JOIN Contributeur on Contributeur.id=Avis.contributeur\
    JOIN Contribution on Contribution.contributeur = Contributeur.id\
    JOIN projet ON projet.id=Avis.projet\
    JOIN Projet_Social on projet.id=Projet_Social.id_p\
    JOIN Projet_socialONG on Projet_Social.id_p=Projet_SocialONG.projet\
    JOIN ONG on Projet_socialONG.ONG=ONG.NEU\
    WHERE ONG.nom='Amnesty Internat.' AND Contribution.montant > 50"
        
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Error as e:
        print("[LOGS] Error request 2")
        return False

    # Fetch data line by line
    raw = cur.fetchone()
    while raw:
        print (raw[0])
        raw = cur.fetchone()

    return True

def select3(conn):
    sql = "SELECT p.id ,COUNT(DISTINCT c.contributeur) AS nb_contributeurs\
    FROM Projet p\
    JOIN Contribution c ON p.id=c.projet\
    JOIN Contributeur contrib ON contrib.id=c.contributeur\
    JOIN Contrepartie_physique cp_p ON c.id=cp_p.id_c\
    JOIN Transporteur t ON cp_p.transporteur=t.nom\
    WHERE(p.incubateur IS NOT NULL AND t.nom='Chronopost')\
    GROUP BY p.id"

    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Error as e:
        print("[LOGS] Error request 3")
        return False

    # Fetch data line by line
    raw = cur.fetchone()
    while raw:
        print (f"id : {raw[0]}, count : {raw[1]}")
        raw = cur.fetchone()
    return True
