@startuml

@startuml
skinparam linetype ortho

class Projet {
    titre : varchar[20] {key}
    description : text
    objectif : float
    lancement : date {key}
    type : {"Projet_Techno", "Projet_Artis", "Projet_Social""}
    type_data : {Projet_Techno, Projet_Artis, Projet_Social}
    membres : Membre
    avis : Avis
}

class Incubateur {
    nom: varchar[20] {key}
    création : integer[4]
    budget : float
}

Incubateur "0..1" --> "*" Projet : Soutient

class Projet_Techno <<DataType>> {
    innovation : text
}
class Projet_Artis <<DataType>> {
    médium : text
}
class Projet_Social <<DataType>> {
    région : text
    ONG : ONG
}
class ONG <<DataType>> {
    NEU : integer {key}
    nom : varchar[20]
    pays : varchar[20]
}

class Membre <<DataType>> {
    prenom : varchar[20]
    pays : varchar[10]
    rôle : Rôle
}

class Contributeur <<DataType>> {
    pseudo : varchar[20] {unique}
    mail : varchar[50]
}

enum Rôle {
    chef de projet
    développeur
    designer
    community manager
}

note bottom of Rôle : à titre indicatif

class Contribution {
    date : datetime {key}
    montant : float
    contributeurs : Contributeur
}

Projet *-- "*" Contribution

class Avis <<DataType>> {
    date : date
    note : integer[1..5]
    texte : text
}

abstract Contrepartie {
}

class Contrepartie_Numérique {
    format : varchar[10]
    tailleFichier : integer
}

class Contrepartie_Physique {
    poids : float
    fraisLivraison : float
    transporteur : Transporteur
}

class Transporteur <<DataType>> {
    nom : varchar[20] {key}
    delai : integer
}

Contribution "1-1"--> "0..1" Contrepartie : Inclue
Contrepartie <|-- Contrepartie_Numérique
Contrepartie <|-- Contrepartie_Physique
@enduml

@enduml