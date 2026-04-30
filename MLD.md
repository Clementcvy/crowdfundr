Choix de modélisation : 

On choisit de transformer Contrepartie par référence, car on n’a pas un héritage semi-complet et l’association sur la classe mère est complexe.
On choisit de transformer Projet par référence, car on n’a pas un héritage semi-complet et l’association sur la classe mère est complexe.
On choisit de transformer Personne par les classes filles, car on a un héritage abstrait et l’association sur la classe mère n’est pas complexe.
On ajoute une clé artificielle id dans Projet pour éviter une clé composée
On a qu'un seul avis par contributeur pour un projet donné

Relations : 

ONG(#NEU: int, nom: varchar[20], pays: varchar[20]) nom et pays NOT NULL

Transporteur(#nom: varchar[20], delai: int) delai NOT NULL

Incubateur(#nom: varchar[20], création: int[4], budget: float) création et budget NOT NULL

Projet(#id: int, titre: varchar[20], description: text, objectif: float, lancement: Date, incubateur => Incubateur)
(titre, lancement) UNIQUE NOT NULL AND description et objectif NOT NULL

Projet_social(#id_p => Projet, region: text)
region NOT NULL

Projet_techno(#id_p => Projet, innovation: text)
innovation NOT NULL

Projet_artis(#id_p => Projet, medium: text)
medium NOT NULL

Contributeur(#id: int, nom: varchar[20], naissance: Date, pseudo: varchar[20], mail: varchar[50])
nom, naissance, mail NOT NULL AND pseudo UNIQUE

Contribution(#id : int, date: DateTime, montant: float, projet => Projet, contributeur => Contributeur)
montant, projet et contributeur NOT NULL

Contrepartie(#contribution => Contribution)

Contrepartie_physique(#contribution => Contrepartie, poids: float, fraisLivraison: float, transporteur => Transporteur)
poids, fraisLivraison et transporteur NOT NULL

Contrepartie_numérique(#contribution => Contrepartie, format: varchar[10], tailleFichier: int)
format et tailleFichier NOT NULL

Projet_socialONG(#Projet_social => Projet_social, #ONG => ONG)

Membre(#id: int, nom: varchar[20], naissance: Date, prenom: varchar[20], pays: varchar[10])
nom, naissance, prenom et pays NOT NULL

Avis(#projet => Projet, #contributeur => Contributeur, date: Date, note: int, texte: text)
avis, note et texte NOT NULL AND 1 <= note <= 5

MembreProjet(#projet => Projet, #membre => Membre,
rôle: {'chef de projet', 'développeur', 'designer', 'community manager'})
rôle NOT NULL 

Contraintes : 

Intersection(Projection(Contrepartie_physique, contribution), Projection(Contrepartie_numérique, contribution)) = {}

Intersection(Projection(Projet_social, id), Projection(Projet_techno, id)) = {} AND Intersection(Projection(Projet_social, id), Projection(Projet_artis, id)) = {} AND Intersection(Projection(Projet_techno, id), Projection(Projet_artis, id)) = {}

Intersection(Projection(Contributeur, nom, naissance), Projection(Membre, nom, naissance)) = {}

### Le contributeur doit avoir contribué pour donner un avis
Projection(Avis, projet, contributeur) ⊆ Projection(Contribution, projet, contributeur) 

Projection(Projet, id) = Projection(MembreProjet, projet)

Projection(Projet, id) =
Projection(Projet_social, id)
UNION Projection(Projet_techno, id)
UNION Projection(Projet_artis, id)

Projection(Contrepartie, contribution) =
Projection(Contrepartie_physique, contribution)
UNION Projection(Contrepartie_numérique, contribution)