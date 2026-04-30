

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