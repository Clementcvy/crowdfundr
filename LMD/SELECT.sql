-- Quels projets artistiques font intervenir à la fois Hideo Kojima et Yoji Shinkawa (membres d'équipe) et ont dépassé leur objectif financier (somme des contributions > objectif) ?

SELECT DISTINCT pa.id_p AS id_p
FROM Projet_artis pa
JOIN Projet p ON p.id = pa.id_p
WHERE (
    SELECT SUM(c.montant)
    FROM Contribution c
    JOIN Membre m ON m.id = c.membre
    WHERE c.projet = p.id
      AND m.nom = 'Shinkawa'
      AND m.prenom = 'Yoji'
) >= p.objectif 
AND pa.id_p IN (
    SELECT DISTINCT pa2.id_p
    FROM Projet_artis pa2
    JOIN Projet p2 ON p2.id = pa2.id_p
    WHERE (
        SELECT SUM(c.montant)
        FROM Contribution c
        JOIN Membre m ON m.id = c.membre
        WHERE c.projet = p2.id
          AND m.nom = 'Kojima'
          AND m.prenom = 'Hideo'
    ) >= p2.objectif
);

-- Quelle est la moyenne des notes des projets sociaux qui sont soutenus par l'ONG nommée
-- Amnesty International, en ne prenant en compte que les utilisateurs ayant apporté une
-- contribution supérieure à 50 euros sur ces projets ?

select AVG(note) from Avis
JOIN Contributeur on Contributeur.id=Avis.contributeur
JOIN Contribution on Contribution.contributeur = Contributeur.id
JOIN projet ON projet.id=Avis.projet
JOIN Projet_Social on projet.id=Projet_Social.id_p
JOIN Projet_socialONG on Projet_Social.id_p=Projet_SocialONG.projet
JOIN ONG on Projet_socialONG.ONG=ONG.NEU
WHERE ONG.nom='Amnesty Internat.' AND Contribution.montant > 50;


--Pour chaque projet accompagné par un incubateur, combien d'utilisateurs distincts
--ont réclamé au moins une contrepartie physique expédiée via le transporteur 
--"Chronopost" lors de leurs contributions ?
SELECT p.id ,COUNT(DISTINCT c.contributeur) AS nb_contributeurs
FROM Projet p
JOIN Contribution c ON p.id=c.projet
JOIN Contributeur contrib ON contrib.id=c.contributeur
JOIN Contrepartie_physique cp_p ON c.id=cp_p.id_c
JOIN Transporteur t ON cp_p.transporteur=t.nom
WHERE(p.incubateur IS NOT NULL AND t.nom='Chronopost')
GROUP BY p.id;



--Requêtes inventées:
--4)Afficher le nom et le pays de toutes les ONG
SELECT nom, pays 
FROM ONG;
--5)Trouver les incubateurs créés après 2010
SELECT nom, creation, budget 
FROM Incubateur 
WHERE creation > 2010;
--6)Lister les projets qui ont un objectif financier supérieur à 5000 euros 
SELECT titre, objectif 
FROM Projet 
WHERE objectif > 5000;
--7)Afficher les transporteurs triés par délai de livraison (du plus rapide au plus long)
SELECT nom, delai 
FROM Transporteur 
ORDER BY delai ASC;
--8)Trouver le pseudo et l'e-mail des contributeurs nés après 1990
SELECT pseudo, mail 
FROM Contributeur 
WHERE naissance > '1990-12-31';
--9)Afficher les détails des contreparties numériques au format PDF
SELECT id_c, format, taille 
FROM Contrepartie_numerique 
WHERE format = 'PDF';
--10)Lister les titres et dates de lancement des projets incubés à "Station F"
SELECT titre, lancement 
FROM Projet 
WHERE incubateur = 'Station F';
--11)Trouver le prénom et le nom des membres de projet originaires du Japon
SELECT prenom, nom 
FROM Membre 
WHERE pays = 'Japon';
--12)Afficher les avis ayant reçu la note maximale de 5
SELECT texte, note 
FROM Avis 
WHERE note = 5;
--13)Compter le nombre d'ONG par pays
SELECT pays, COUNT(*) AS nombre_ong 
FROM ONG 
GROUP BY pays;
--14)Calculer le montant total récolté pour chaque projet (par ID de projet)
SELECT projet, SUM(montant) AS total_recolte 
FROM Contribution 
GROUP BY projet;
--15)Trouver la note moyenne attribuée à chaque projet
SELECT projet, AVG(note) AS note_moyenne 
FROM Avis 
GROUP BY projet;
--16)Compter le nombre de projets rattachés à chaque incubateur
SELECT incubateur, COUNT(*) AS nb_projets 
FROM Projet 
WHERE incubateur IS NOT NULL 
GROUP BY incubateur;
--17)Compter le nombre de contreparties physiques gérées par chaque transporteur
SELECT transporteur, COUNT(*) AS nb_colis 
FROM Contrepartie_physique 
GROUP BY transporteur;
--18) Calculer le budget moyen des incubateurs en fonction de leur année de création
SELECT creation, AVG(budget) AS budget_moyen 
FROM Incubateur 
GROUP BY creation;
--19)Compter le nombre de contreparties numériques pour chaque type de format (PDF, MP3, etc.)
SELECT format, COUNT(*) AS nb_fichiers 
FROM Contrepartie_numerique 
GROUP BY format;
--20)Trouver le nombre total de contributions effectuées par chaque contributeur (par ID de contributeur)
SELECT contributeur, COUNT(*) AS nb_participations 
FROM Contribution 
GROUP BY contributeur;
