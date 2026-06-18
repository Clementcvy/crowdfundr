CREATE SCHEMA nosql;

CREATE TABLE nosql.Incubateur (
    nom VARCHAR(20) PRIMARY KEY,
    creation INT NOT NULL, -- Représente l'année (int[4])
    budget FLOAT NOT NULL,
CONSTRAINT annee CHECK (creation BETWEEN 1 AND 9999)
);

CREATE TYPE nosql.typeProjet AS ENUM('projet_techno', 'projet_social', 'projet_artis');

CREATE TABLE nosql.Projet (
    id INT PRIMARY KEY,
    titre VARCHAR(20) NOT NULL,
    descr TEXT NOT NULL,
    objectif FLOAT NOT NULL,
    lancement DATE NOT NULL,
    incubateur VARCHAR(20),
    type_projet nosql.typeProjet NOT NULL,
    innovation TEXT,
    region TEXT,
    medium TEXT,
    membre JSON NOT NULL,
    avis JSON NOT NULL,
CONSTRAINT projet_incubateur FOREIGN KEY (incubateur) REFERENCES nosql.Incubateur(nom)
    -- Si typeProjet == 'projet_techno' : innovation NOT NULL, region & medium NULL
    -- Si typeProjet == 'projet_social' : region NOT NULL, innovation & medium NULL
    -- Si typeProjet == 'projet_artis' : medium NOT NULL, region & innovation NULL
);

CREATE TABLE nosql.Contributeur (
    id INT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    naissance DATE NOT NULL,
    pseudo VARCHAR(20) UNIQUE NOT NULL,
    mail VARCHAR(50) NOT NULL
);

CREATE TABLE nosql.Contribution (
    id INT PRIMARY KEY,
    date_c TIMESTAMP NOT NULL,
    montant FLOAT NOT NULL,
    projet INT NOT NULL,
    contributeur INT NOT NULL,
CONSTRAINT contrib_projet FOREIGN KEY (projet) REFERENCES nosql.Projet(id),
CONSTRAINT contrib_contributeur FOREIGN KEY (contributeur) REFERENCES nosql.Contributeur(id)
);

CREATE TABLE nosql.Contrepartie (
    id_c INT PRIMARY KEY,
CONSTRAINT contrib FOREIGN KEY (id_c) REFERENCES nosql.Contribution(id)
);

CREATE TABLE nosql.Contrepartie_physique (
    id_c INT PRIMARY KEY,
    poids FLOAT NOT NULL,
    frais FLOAT NOT NULL,
    transporteur JSON NOT NULL,
CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES nosql.Contrepartie(id_c)
);

CREATE TABLE nosql.Contrepartie_numerique (
    id_c INT PRIMARY KEY,
    format VARCHAR(10) NOT NULL,
    taille INT NOT NULL,
CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES nosql.Contrepartie(id_c)
);