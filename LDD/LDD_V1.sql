select note from Avis
JOIN Contributeur on Contributeur.id=Avis.contributeur
JOIN Contribution on Contribution.contributeur = Contributeur.id
JOIN projet ON projet.id=Avis.projet
JOIN Projet_Social on projet.id=Projet_Social.id_p
JOIN Projet_socialONG on Projet_Social.id_p=Projet_SocialONG.projet
WHERE Projet_socialONGONG="Amnesty Internat."
AND Contribution.montant > 50;