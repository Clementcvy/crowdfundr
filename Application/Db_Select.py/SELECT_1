# Created on iPad.

#!/usr/bin/python3

# http://initd.org/psycopg/docs/usage.html

import psycopg2

HOST = "localhost"
USER = "me"
PASSWORD = "secret"
DATABASE = "mydb"

# Open connection
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

# Open a cursor to send SQL commands
cur = conn.cursor()

# Execute a SQL SELECT command
sql = "SELECT DISTINCT pa.id_p
FROM Projet_artis pa
JOIN Projet p ON p.id = pa.id_p
JOIN MembreProjet mp1 ON mp1.projet = p.id
JOIN Membre m1 ON m1.id = mp1.membre
JOIN MembreProjet mp2 ON mp2.projet = p.id
JOIN Membre m2 ON m2.id = mp2.membre
WHERE m1.nom = 'Shinkawa'
  AND m1.prenom = 'Yoji'
  AND m2.nom = 'Kojima'
  AND m2.prenom = 'Hideo'
  AND (
      SELECT SUM(c.montant)
      FROM Contribution c
      WHERE c.projet = p.id
  ) >= p.objectif
"
cur.execute(sql)

# Fetch data line by line
raw = cur.fetchone()
while raw:
    print (raw[0])
    print (raw[1])
    raw = cur.fetchone()

# Close connection
conn.close()
