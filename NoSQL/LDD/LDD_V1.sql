CREATE TABLE Incubateur (

    nom VARCHAR(20) PRIMARY KEY,

    creation INT NOT NULL, -- Représente l'année (int[4])

    budget FLOAT NOT NULL,

    CONSTRAINT annee CHECK (creation BETWEEN 1 AND 9999)

);

CREATE TYPE type_projet as ENUM('projet_techno', 'projet_social', 'projet_artis');


CREATE TABLE Projet (

    id INT PRIMARY KEY,

    titre VARCHAR(20) NOT NULL,

    descr TEXT NOT NULL,

    objectif FLOAT NOT NULL,

    lancement DATE NOT NULL,

    incubateur VARCHAR(20),

    type_projet 

    membre   JSON NOT NULL 

    avis JSON NOT NULL

    CONSTRAINT projet_incubateur FOREIGN KEY (incubateur) REFERENCES Incubateur(nom)

);   


CREATE TABLE Contribution (

    id INT PRIMARY KEY,

    date_c TIMESTAMP NOT NULL,

    montant FLOAT NOT NULL,

    projet INT NOT NULL,

    contributeur JSON NOT NULL,

    CONSTRAINT contrib_projet FOREIGN KEY (projet) REFERENCES Projet(id)

);


CREATE TABLE Contrepartie (

    id_c INT PRIMARY KEY,

    CONSTRAINT contrib FOREIGN KEY (id_c) REFERENCES Contribution(id)

);


CREATE TABLE Contrepartie_physique (

    id_c INT PRIMARY KEY,

    poids FLOAT NOT NULL,

    frais FLOAT NOT NULL,

    transporteur JSON NOT NULL,

    

    CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES Contrepartie(id_c)

);


CREATE TABLE Contrepartie_numerique (

    id_c INT PRIMARY KEY,

    format VARCHAR(10) NOT NULL,

    taille INT NOT NULL,

    CONSTRAINT contrepartie FOREIGN KEY (id_c) REFERENCES Contrepartie(id_c)

);