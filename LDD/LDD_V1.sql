CREATE SCHEMA sql;

CREATE TABLE sql.ONG (
    NEU INT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    pays VARCHAR(20) NOT NULL
);
CREATE TABLE sql.Transporteur (
    nom VARCHAR(20) PRIMARY KEY,
    delai INT NOT NULL
);
CREATE TABLE sql.Incubateur (
    nom VARCHAR(20) PRIMARY KEY,
    creation INT NOT NULL,
    budget FLOAT NOT NULL,
CONSTRAINT annee CHECK (creation BETWEEN 1 AND 9999)
);
CREATE TABLE sql.Projet (
    id INT PRIMARY KEY,
    titre VARCHAR(20) NOT NULL,
    descr TEXT NOT NULL,
    objectif FLOAT NOT NULL,
    lancement DATE NOT NULL,
    incubateur VARCHAR(20),
CONSTRAINT projet_incubateur FOREIGN KEY (incubateur) REFERENCES sql.Incubateur(nom),
CONSTRAINT projet_titre_lancement UNIQUE (titre, lancement)
);
CREATE TABLE sql.Projet_social (
    id_p INT PRIMARY KEY,
    region TEXT NOT NULL,
CONSTRAINT psocial_projet FOREIGN KEY (id_p) REFERENCES sql.Projet(id) ON DELETE CASCADE
);
CREATE TABLE sql.Projet_techno (
    id_p INT PRIMARY KEY,
    innovation TEXT NOT NULL,
CONSTRAINT ptechno_projet FOREIGN KEY (id_p) REFERENCES sql.Projet(id) ON DELETE CASCADE
);
CREATE TABLE sql.Projet_artis (
    id_p INT PRIMARY KEY,
    medium TEXT NOT NULL,
CONSTRAINT partis_projet FOREIGN KEY (id_p) REFERENCES sql.Projet(id) ON DELETE CASCADE
);
CREATE TABLE sql.Contributeur (
    id INT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    naissance DATE NOT NULL,
    pseudo VARCHAR(20) UNIQUE NOT NULL,
    mail VARCHAR(50) NOT NULL
);
CREATE TABLE sql.Contribution (
    id INT PRIMARY KEY,
    date_c TIMESTAMP NOT NULL,
    montant FLOAT NOT NULL,
    projet INT NOT NULL,
    contributeur INT NOT NULL,
CONSTRAINT contrib_projet FOREIGN KEY (projet) REFERENCES sql.Projet(id) ON DELETE CASCADE,
CONSTRAINT contrib FOREIGN KEY (contributeur) REFERENCES sql.Contributeur(id)
);
CREATE TABLE sql.Contrepartie (
    id_c INT PRIMARY KEY,
CONSTRAINT contrib FOREIGN KEY (id_c) REFERENCES sql.Contribution(id) ON DELETE CASCADE
);
CREATE TABLE sql.Contrepartie_physique (
    id_c INT PRIMARY KEY,
    poids FLOAT NOT NULL,
    frais FLOAT NOT NULL,
    transporteur VARCHAR(20) NOT NULL,
CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES sql.Contrepartie(id_c) ON DELETE CASCADE,
CONSTRAINT transporteur FOREIGN KEY (transporteur) REFERENCES sql.Transporteur(nom)
);
CREATE TABLE sql.Contrepartie_numerique (
    id_c INT PRIMARY KEY,
    format VARCHAR(10) NOT NULL,
    taille INT NOT NULL,
CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES sql.Contrepartie(id_c) ON DELETE CASCADE
);

CREATE TABLE sql.Projet_socialONG(
    projet INT,
    ONG INT,
CONSTRAINT cle_ong FOREIGN KEY (ONG) REFERENCES sql.ONG(NEU),
CONSTRAINT cle_projet FOREIGN KEY (projet) REFERENCES sql.Projet_social(id_p) ON DELETE CASCADE,
CONSTRAINT cle_projet_ONG PRIMARY KEY(projet,ONG)
);
CREATE TABLE sql.Membre (
    id INT PRIMARY KEY,
    nom VARCHAR(20) NOT NULL,
    naissance DATE NOT NULL,
    prenom VARCHAR(20) NOT NULL,
    pays VARCHAR(10) NOT NULL
);
CREATE TABLE sql.Avis(
    projet INT,
    contributeur INT,
    date_a DATE NOT NULL,
    note INT NOT NULL,
    texte TEXT NOT NULL,
CONSTRAINT avis_projet FOREIGN KEY (projet) REFERENCES sql.Projet(id) ON DELETE CASCADE,
CONSTRAINT avis_contrib FOREIGN KEY (contributeur) REFERENCES sql.Contributeur(id),
CONSTRAINT cle_avis PRIMARY KEY(projet,contributeur),
CONSTRAINT validation_note CHECK(note BETWEEN 1 AND 5)
);
CREATE TYPE sql.roleMembre as ENUM('chef de projet', 'développeur', 'designer', 'community manager');
CREATE TABLE sql.MembreProjet(
    projet INT,
    membre INT,
CONSTRAINT cle_projet FOREIGN KEY (projet) REFERENCES sql.Projet(id) ON DELETE CASCADE,
CONSTRAINT cle_membre FOREIGN KEY (membre) REFERENCES sql.Membre(id),
    role_m sql.roleMembre NOT NULL,
CONSTRAINT cle_membre_projet PRIMARY KEY(projet,membre)
);