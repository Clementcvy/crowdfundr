
class Projet {
    titre : varchar[20] {key}
    description : text
    objectif : float
    lancement : date {key}
    type : {"Projet_Techno", "Projet_Artis", "Projet_Social""}
    innovation : text
    region : text
    medium : text
    membres : JSON
    avis : JSON
}

class Incubateur {
    nom: varchar[20] {key}
    création : integer[4]
    budget : float
}

Incubateur "0..1" --> "*" Projet : Soutient

class Contributeur {
    pseudo : varchar[20] {unique}
    mail : varchar[50]
}

Projet "*" <-- "*" Contributeur : contribue

Contributeur "1" <-- "*" Contribution : appartient

class Contribution {
    date : datetime {key}
    montant : float
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
    transporteur : JSON
}

Contribution "1-1"--> "0..1" Contrepartie : Inclue
Contrepartie <|-- Contrepartie_Numérique
Contrepartie <|-- Contrepartie_Physique