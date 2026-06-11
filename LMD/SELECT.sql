-- Quels projets artistiques font intervenir à la fois Hideo Kojima et Yoji Shinkawa (membres d'équipe) et ont dépassé leur objectif financier (somme des contributions > objectif) ?

SELECT DISTINCT pa.id_p
FROM sql.Projet_artis pa
JOIN sql.Projet p ON p.id = pa.id_p
JOIN sql.MembreProjet mp1 ON mp1.projet = p.id
JOIN sql.Membre m1 ON m1.id = mp1.membre
JOIN sql.MembreProjet mp2 ON mp2.projet = p.id
JOIN sql.Membre m2 ON m2.id = mp2.membre
WHERE m1.nom = 'Shinkawa'
  AND m1.prenom = 'Yoji'
  AND m2.nom = 'Kojima'
  AND m2.prenom = 'Hideo'
  AND (
      SELECT SUM(c.montant)
      FROM sql.Contribution c
      WHERE c.projet = p.id
  ) >= p.objectif;

-- Quelle est la moyenne des notes des projets sociaux qui sont soutenus par l'ONG nommée
-- Amnesty International, en ne prenant en compte que les utilisateurs ayant apporté une
-- contribution supérieure à 50 euros sur ces projets ?

SELECT AVG(note) FROM sql.Avis
JOIN sql.Contributeur ON sql.Contributeur.id = sql.Avis.contributeur
JOIN sql.Contribution ON sql.Contribution.contributeur = sql.Contributeur.id
JOIN sql.Projet ON sql.Projet.id = sql.Avis.projet
JOIN sql.Projet_Social ON sql.Projet.id = sql.Projet_Social.id_p
JOIN sql.Projet_socialONG ON sql.Projet_Social.id_p = sql.Projet_SocialONG.projet
JOIN sql.ONG ON sql.Projet_socialONG.ONG = sql.ONG.NEU
WHERE sql.ONG.nom = 'Amnesty Internat.' AND sql.Contribution.montant > 50;


-- Pour chaque projet accompagné par un incubateur, combien d'utilisateurs distincts
-- ont réclamé au moins une contrepartie physique expédiée via le transporteur 
-- "Chronopost" lors de leurs contributions ?
SELECT p.id, COUNT(DISTINCT c.contributeur) AS nb_contributeurs
FROM sql.Projet p
JOIN sql.Contribution c ON p.id = c.projet
JOIN sql.Contributeur contrib ON contrib.id = c.contributeur
JOIN sql.Contrepartie_physique cp_p ON c.id = cp_p.id_c
JOIN sql.Transporteur t ON cp_p.transporteur = t.nom
WHERE (p.incubateur IS NOT NULL AND t.nom = 'Chronopost')
GROUP BY p.id;



-- Requêtes inventées:
-- 4) Afficher le nom et le pays de toutes les ONG
SELECT nom, pays 
FROM sql.ONG;
-- 5) Trouver les incubateurs créés après 2010
SELECT nom, creation, budget 
FROM sql.Incubateur 
WHERE creation > 2010;
-- 6) Lister les projets qui ont un objectif financier supérieur à 5000 euros 
SELECT titre, objectif 
FROM sql.Projet 
WHERE objectif > 5000;
-- 7) Afficher les transporteurs triés par délai de livraison (du plus rapide au plus long)
SELECT nom, delai 
FROM sql.Transporteur 
ORDER BY delai ASC;
-- 8) Trouver le pseudo et l'e-mail des contributeurs nés après 1990
SELECT pseudo, mail 
FROM sql.Contributeur 
WHERE naissance > '1990-12-31';
-- 9) Afficher les détails des contreparties numériques au format PDF
SELECT id_c, format, taille 
FROM sql.Contrepartie_numerique 
WHERE format = 'PDF';
-- 10) Lister les titres et dates de lancement des projets incubés à "Station F"
SELECT titre, lancement 
FROM sql.Projet 
WHERE incubateur = 'Station F';
-- 11) Trouver le prénom et le nom des membres de projet originaires du Japon
SELECT prenom, nom 
FROM sql.Membre 
WHERE pays = 'Japon';
-- 12) Afficher les avis ayant reçu la note maximale de 5
SELECT texte, note 
FROM sql.Avis 
WHERE note = 5;
-- 13) Compter le nombre d'ONG par pays
SELECT pays, COUNT(*) AS nombre_ong 
FROM sql.ONG 
GROUP BY pays;
-- 14) Calculer le montant total récolté pour chaque projet (par ID de projet)
SELECT projet, SUM(montant) AS total_recolte 
FROM sql.Contribution 
GROUP BY projet;
-- 15) Trouver la note moyenne attribuée à chaque projet
SELECT projet, AVG(note) AS note_moyenne 
FROM sql.Avis 
GROUP BY projet;
-- 16) Compter le nombre de projets rattachés à chaque incubateur
SELECT incubateur, COUNT(*) AS nb_projets 
FROM sql.Projet 
WHERE incubateur IS NOT NULL 
GROUP BY incubateur;
-- 17) Compter le nombre de contreparties physiques gérées par chaque transporteur
SELECT transporteur, COUNT(*) AS nb_colis 
FROM sql.Contrepartie_physique 
GROUP BY transporteur;
-- 18) Calculer le budget moyen des incubateurs en fonction de leur année de création
SELECT creation, AVG(budget) AS budget_moyen 
FROM sql.Incubateur 
GROUP BY creation;
-- 19) Compter le nombre de contreparties numériques pour chaque type de format (PDF, MP3, etc.)
SELECT format, COUNT(*) AS nb_fichiers 
FROM sql.Contrepartie_numerique 
GROUP BY format;
-- 20) Trouver le nombre total de contributions effectuées par chaque contributeur (par ID de contributeur)
SELECT contributeur, COUNT(*) AS nb_participations 
FROM sql.Contribution 
GROUP BY contributeur;