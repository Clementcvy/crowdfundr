-- 1. Avis 
DELETE FROM Avis 
WHERE projet IN (1, 6, 11);

-- 2. Filles contreparties 
DELETE FROM Contrepartie_physique 
WHERE id_c IN (5, 7, 8, 9, 10);

DELETE FROM Contrepartie_numerique 
WHERE id_c IN (1, 2, 3, 4, 6);

-- 3. Contrepartie
DELETE FROM Contrepartie 
WHERE id_c IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

-- 4. Contribution 
DELETE FROM Contribution 
WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

-- 5. Contributeur
DELETE FROM Contributeur 
WHERE id IN (1, 2, 3, 4, 5);

-- 6. MembreProjet 
DELETE FROM MembreProjet 
WHERE projet IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15);

-- 7. Membre
DELETE FROM Membre 
WHERE id IN (1, 2, 3, 4, 5);

-- 8. Projet Social ONG 
DELETE FROM Projet_socialONG 
WHERE projet IN (6, 7, 8, 9, 10);

-- 9. Sous-projets 
DELETE FROM Projet_techno 
WHERE id_p IN (11, 12, 13, 14, 15);

DELETE FROM Projet_social 
WHERE id_p IN (6, 7, 8, 9, 10);

DELETE FROM Projet_artis 
WHERE id_p IN (1, 2, 3, 4, 5);

-- 10. Projet 
DELETE FROM Projet 
WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15);

-- 11. Incubateur
DELETE FROM Incubateur 
WHERE nom IN ('Station F', 'Le Cargo', 'Techstars', 'Y Combinator', 'Plug and Play');

-- 12. Transporteur
DELETE FROM Transporteur 
WHERE nom IN ('Chronopost', 'DHL', 'FedEx', 'UPS', 'La Poste');

-- 13. ONG
DELETE FROM ONG 
WHERE NEU IN (1, 2, 3, 4, 5);
