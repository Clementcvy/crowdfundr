--- ONG
INSERT INTO ONG (NEU, nom, pays) VALUES 
(1, 'Amnesty Internat.', 'Royaume-Uni'),
(2, 'Croix-Rouge', 'France'),
(3, 'MSF', 'Suisse'),
(4, 'WWF', 'Suisse'),
(5, 'Greenpeace', 'Pays-Bas');

-- Transporteur
INSERT INTO Transporteur (nom, delai) VALUES 
('Chronopost', 2),
('DHL', 3),
('FedEx', 5),
('UPS', 4),
('La Poste', 7);

-- Incubateur
INSERT INTO Incubateur (nom, creation, budget) VALUES 
('Station F', 2017, 1000000),
('Le Cargo', 2016, 500000),
('Techstars', 2006, 2000000),
('Y Combinator', 2005, 5000000),
('Plug and Play', 2006, 1500000);

-- Projet
INSERT INTO Projet (id, titre, descr, objectif, lancement, incubateur) VALUES 
-- Projets Artis
(1, 'Tactical Art', 'Expo jeu video', 1000.0, '2026-01-01', 'Le Cargo'),
(2, 'Artisanat 2', 'Peinture', 2000.0, '2026-01-02', 'Station F'),
(3, 'Artisanat 3', 'Sculpture', 3000.0, '2026-01-03', NULL),
(4, 'Artisanat 4', 'Musique', 4000.0, '2026-01-04', NULL),
(5, 'Artisanat 5', 'Cinema', 5000.0, '2026-01-05', NULL),
-- Projets Soc
(6, 'Human Rights', 'Droits Humains', 500.0, '2026-02-01', 'Techstars'),
(7, 'Social 2', 'Ecoles', 600.0, '2026-02-02', 'Station F'),
(8, 'Social 3', 'Eau potable', 700.0, '2026-02-03', NULL),
(9, 'Social 4', 'Agriculture', 800.0, '2026-02-04', NULL),
(10, 'Social 5', 'Refuges', 900.0, '2026-02-05', NULL),
-- Projets Techno
(11, 'Ocean Bot', 'Robot marin', 10000.0, '2026-03-01', 'Y Combinator'),
(12, 'Tech 2', 'IA Medicale', 20000.0, '2026-03-02', 'Plug and Play'),
(13, 'Tech 3', 'Blockchain', 30000.0, '2026-03-03', NULL),
(14, 'Tech 4', 'Energie solaire', 40000.0, '2026-03-04', NULL),
(15, 'Tech 5', 'Domotique', 50000.0, '2026-03-05', NULL);

-- Sous projets
INSERT INTO Projet_artis (id_p, medium) VALUES 
(1, 'Jeu Video'), (2, 'Peinture'), (3, 'Sculpture'), (4, 'Musique'), (5, 'Cinema');

INSERT INTO Projet_social (id_p, region) VALUES 
(6, 'Monde'), (7, 'Europe'), (8, 'Afrique'), (9, 'Asie'), (10, 'Amerique');

INSERT INTO Projet_techno (id_p, innovation) VALUES 
(11, 'Robotique'), (12, 'IA'), (13, 'Web3'), (14, 'Cleantech'), (15, 'IoT');

-- Projet Social ONG
INSERT INTO Projet_socialONG (projet, ONG) VALUES 
(6,1), (7,2), (8,3), (9,4), (10,5);

-- Membre
INSERT INTO Membre (id, nom, naissance, prenom, pays) VALUES 
(1, 'Kojima', '1963-08-24', 'Hideo', 'Japon'),
(2, 'Shinkawa', '1971-12-25', 'Yoji', 'Japon'),
(3, 'Durand', '1985-03-12', 'Marie', 'France'),
(4, 'Smith', '1992-07-20', 'John', 'USA'),
(5, 'Zola', '1978-11-02', 'Emile', 'Italie');

-- MembreProjet
INSERT INTO MembreProjet (projet, membre, role_m) VALUES 
(1, 1, 'chef de projet'), (1, 2, 'designer'),
(2, 3, 'développeur'), (3, 4, 'designer'), (4, 5, 'community manager'), (5, 1, 'chef de projet'),
(6, 2, 'designer'), (7, 3, 'développeur'), (8, 4, 'designer'), (9, 5, 'community manager'),
(10, 1, 'chef de projet'), (11, 2, 'designer'), (12, 3, 'développeur'), (13, 4, 'designer'),
(14, 5, 'community manager'), (15, 3, 'chef de projet');

-- Contributeur
INSERT INTO Contributeur (id, nom, naissance, pseudo, mail) VALUES 
(1, 'Dupont', '1990-01-01', 'dupondt', 'd@mail.com'),
(2, 'Martin', '1988-05-15', 'marty', 'm@mail.com'),
(3, 'Bernard', '1995-10-10', 'berny', 'b@mail.com'),
(4, 'Petit', '1980-12-31', 'tipeu', 'p@mail.com'),
(5, 'Leroy', '2000-06-15', 'roy', 'l@mail.com');

-- Contribution
INSERT INTO Contribution (id, date_c, montant, projet, contributeur) VALUES 
(1, '2026-01-05 10:00:00', 600.0, 1, 1),
(2, '2026-01-06 12:00:00', 500.0, 1, 2), 
(3, '2026-02-05 09:00:00', 100.0, 6, 3),
(4, '2026-02-06 14:00:00', 80.0,  6, 4),
(5, '2026-01-10 16:00:00', 20.0,  2, 5),
(6, '2026-02-15 10:00:00', 30.0,  7, 1),
(7, '2026-03-10 11:00:00', 40.0, 11, 2),
(8, '2026-03-15 14:00:00', 50.0, 12, 3),
(9, '2026-01-20 18:00:00', 60.0,  1, 4),
(10,'2026-02-20 09:00:00', 70.0,  6, 5);

-- Contrepartie
INSERT INTO Contrepartie (id_c) VALUES 
(1), (2), (3), (4), (5), (6), (7), (8), (9), (10);

-- Filles contreparties
INSERT INTO Contrepartie_numerique (id_c, format, taille) VALUES 
(1, 'PDF', 10), (2, 'MP3', 20), (3, 'MP4', 30), (4, 'ZIP', 40), (6, 'RAR', 50);

INSERT INTO Contrepartie_physique (id_c, poids, frais, transporteur) VALUES 
(5, 1.0, 5.0, 'Chronopost'),
(7, 2.0, 10.0, 'Chronopost'),
(8, 3.0, 15.0, 'Chronopost'),
(9, 4.0, 20.0, 'Chronopost'),
(10, 5.0, 25.0, 'Chronopost');

-- Avis
INSERT INTO Avis (projet, contributeur, date_a, note, texte) VALUES 
(1, 1, '2026-01-10', 5, 'Merveilleux'),
(1, 2, '2026-01-15', 5, 'Incroyable'),
(6, 3, '2026-03-01', 4, 'Tres important'),
(6, 4, '2026-04-01', 5, 'Bravo Amnesty'),
(11, 2, '2026-03-20', 3, 'Techno sympa');