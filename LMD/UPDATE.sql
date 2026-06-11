-- 1
UPDATE sql.Projet 
SET descr = 'changer le monde'
WHERE descr = 'sauver la planète' AND titre = 'GREEN';
-- 2
UPDATE sql.Membre 
SET prenom = 'Jean-Michel'
WHERE prenom = 'J-M';
-- 3. 
UPDATE sql.Transporteur 
SET delai = 800
WHERE nom = 'La Poste';
-- 4. 
UPDATE sql.Incubateur 
SET budget = 0
WHERE nom = 'digital school';