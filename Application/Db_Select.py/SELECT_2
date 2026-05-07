# Created 
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
sql = "select AVG(note) from Avis
JOIN Contributeur on Contributeur.id=Avis.contributeur
JOIN Contribution on Contribution.contributeur = Contributeur.id
JOIN projet ON projet.id=Avis.projet
JOIN Projet_Social on projet.id=Projet_Social.id_p
JOIN Projet_socialONG on Projet_Social.id_p=Projet_SocialONG.projet
JOIN ONG on Projet_socialONG.ONG=ONG.NEU
WHERE ONG.nom='Amnesty Internat.' AND Contribution.montant > 50


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
