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
sql = " SELECT *
FROM Projet
LEFT JOIN Incubateur ON Projet.incubateur = Incubateur.nom
LEFT JOIN Projet_social ON Projet.id = Projet_social.id_p
LEFT JOIN Projet_techno ON Projet.id = Projet_techno.id_p
LEFT JOIN Projet_artis ON Projet.id = Projet_artis.id_p
LEFT JOIN Projet_socialONG ON Projet_social.id_p = Projet_socialONG.projet
LEFT JOIN ONG ON Projet_socialONG.ONG = ONG.
LEFT JOIN MembreProjet ON Projet.id = MembreProjet.projet
LEFT JOIN Membre ON MembreProjet.membre = Membre.id
LEFT JOIN Contribution ON Projet.id = Contribution.projet
LEFT JOIN Contributeur ON Contribution.contributeur = Contributeur.id
LEFT JOIN Avis ON Projet.id = Avis.projet AND Contributeur.id = Avis.contributeur
LEFT JOIN Contrepartie ON Contribution.id = Contrepartie.id_c
LEFT JOIN Contrepartie_physique ON Contrepartie.id_c = Contrepartie_physique.id_c
LEFT JOIN Transporteur ON Contrepartie_physique.transporteur = Transporteur.nom
LEFT JOIN Contrepartie_numerique ON Contrepartie.id_c = Contrepartie_numerique.id_c;
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
