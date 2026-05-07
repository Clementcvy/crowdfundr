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
sql = "SELECT p.id ,COUNT(DISTINCT c.contributeur) AS nb_contributeurs
FROM Projet p
JOIN Contribution c ON p.id=c.projet
JOIN Contributeur contrib ON contrib.id=c.contributeur
JOIN Contrepartie_physique cp_p ON c.id=cp_p.id_c
JOIN Transporteur t ON cp_p.transporteur=t.nom
WHERE(p.incubateur IS NOT NULL AND t.nom='Chronopost')
GROUP BY p.id
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

