CREATE TABLE ONG (
    NEU INT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    pays VARCHAR(20) NOT NULL
);

CREATE TABLE Transporteur (
    nom VARCHAR(20) PRIMARY KEY,
    delai INT NOT NULL
);

CREATE TABLE Incubateur (
    nom VARCHAR(20) PRIMARY KEY,
    creation INT NOT NULL, -- Représente l'année (int[4])
    budget FLOAT NOT NULL,
    CONSTRAINT annee CHECK (creation BETWEEN 1 AND 9999)
);

CREATE TABLE Projet (
    id INT PRIMARY KEY,
    titre VARCHAR(20) NOT NULL,
    descr TEXT NOT NULL,
    objectif FLOAT NOT NULL,
    lancement DATE NOT NULL,
    incubateur VARCHAR(20),
    CONSTRAINT projet_incubateur FOREIGN KEY (incubateur) REFERENCES Incubateur(nom),
    CONSTRAINT projet_titre_lancement UNIQUE (titre, lancement)
);

CREATE TABLE Projet_social (
    id_p INT PRIMARY KEY,
    region TEXT NOT NULL,
    CONSTRAINT psocial_projet FOREIGN KEY (id_p) REFERENCES Projet(id) 
);

CREATE TABLE Projet_techno (
    id_p INT PRIMARY KEY,
    innovation TEXT NOT NULL,
    CONSTRAINT ptechno_projet FOREIGN KEY (id_p) REFERENCES Projet(id)
);

CREATE TABLE Projet_artis (
    id_p INT PRIMARY KEY,
    medium TEXT NOT NULL,
    CONSTRAINT partis_projet FOREIGN KEY (id_p) REFERENCES Projet(id) 
);

CREATE TABLE Contributeur (
    id INT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    naissance DATE NOT NULL,
    pseudo VARCHAR(20) UNIQUE NOT NULL,
    mail VARCHAR(50) NOT NULL
);

CREATE TABLE Contribution (
    id INT PRIMARY KEY,
    date_c TIMESTAMP NOT NULL,
    montant FLOAT NOT NULL,
    projet INT NOT NULL,
    contributeur INT NOT NULL,
    CONSTRAINT contrib_projet FOREIGN KEY (projet) REFERENCES Projet(id),
    CONSTRAINT contrib FOREIGN KEY (contributeur) REFERENCES Contributeur(id)
);

CREATE TABLE Contrepartie (
    id_c INT PRIMARY KEY,
    CONSTRAINT contrib FOREIGN KEY (id_c) REFERENCES Contribution(id)
);

CREATE TABLE Contrepartie_physique (
    id_c INT PRIMARY KEY,
    poids FLOAT NOT NULL,
    frais FLOAT NOT NULL,
    transporteur VARCHAR(20) NOT NULL,
    CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES Contrepartie(id_c),
    CONSTRAINT transporteur FOREIGN KEY (transporteur) REFERENCES Transporteur(nom)
);

CREATE TABLE Contrepartie_numerique (
    id_c INT PRIMARY KEY,
    format VARCHAR(10) NOT NULL,
    taille INT NOT NULL,
    CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES Contrepartie(id_c)
);

CREATE TABLE Projet_socialONG( --Association *-*
    projet INT,
    ONG INT,
	CONSTRAINT cle_ong FOREIGN KEY (projet) REFERENCES ONG(NEU),
	CONSTRAINT cle_projet FOREIGN KEY (ONG) REFERENCES Projet_social(id_p),
    CONSTRAINT cle_projet_ONG PRIMARY KEY(projet,ONG)
);

CREATE TABLE Membre (
    id INT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    naissance DATE NOT NULL,
    prenom VARCHAR(20) NOT NULL,
    pays VARCHAR(10) NOT NULL
);

CREATE TABLE Avis(
    projet INT,
    contributeur INT,
    date_a DATE NOT NULL,
    note INT NOT NULL,
    texte TEXT NOT NULL,
    CONSTRAINT avis_projet FOREIGN KEY (projet) REFERENCES Projet(id),
    CONSTRAINT avis_contrib FOREIGN KEY (contributeur) REFERENCES Contributeur(id),
    CONSTRAINT cle_avis PRIMARY KEY(projet,contributeur),
    CONSTRAINT validation_note CHECK(note BETWEEN 1 AND 5)
);

CREATE TYPE roleMembre as ENUM('chef de projet', 'développeur', 'designer', 'community manager');

CREATE TABLE MembreProjet( -- Association *-*
    projet INT,
    membre INT,
	CONSTRAINT cle_projet FOREIGN KEY (projet) REFERENCES Projet(id),
	CONSTRAINT cle_membre FOREIGN KEY (membre) REFERENCES Membre(id),
    role_m roleMembre NOT NULL,
    CONSTRAINT cle_membre_projet PRIMARY KEY(projet,membre)
);