Choix de modélisation : 

On choisi de transformer Contrepartie par référence, car on a pas un héritage semi-complet et l'association sur la classe mère est complexe
On choisi de transformer Projet par référence, car on a pas un héritage semi-complet et l'association sur la classe mère est complexe
On choisi de transformer Personne par les classes filles, car on a un héritage abstrait et l'association sur la classe mère n'est pas complexe

Relations : 

ONG(#NEU: int, nom: varchar[20], pays: varchar[20]) nom et pays NOT NULL
Transporteur(#nom: varchar[20], delai: int) delai NOT NULL
Incubateur(#nom: varchar[20], création: int[4], budget: float) création et budget NOT NULL
Projet(#id: int, titre: varchar[20], description: text, objectif: float, lancement: Date, incubateur=>Incubateur) (titre, lancement) KEY AND decription et objectif NOT NULL
Projet_social(#id=>Projet, region: text)
Projet_techno(#id=>Projet, innovation: text)
Projet_artis(#id=>Projet, medium: text)
Contributeur(#id: int, nom: varchar[20], naissance: Date, pseudo: varchar[20], mail: varchar[50]) nom, naissance, mail NOT NULL AND pseudo KEY
Contribution(#date: Date, montant: float, projet=>Projet, contributeur=>Contributeur) montant, projet et contributeur NOT NULL
Contrepartie(#id: int, contribution=>Conribution) contribution NOT NULL
Contrepartie_physique(#id=>Contrepartie, poids: float, fraisLivraison: float, transporteur=>Transporteur) poids, fraisLivraison et transporteur NOT NULL
Contrepartie_numérique(#id=>Contrepartie, format: varchar[10], tailleFichier: int) format et tailleFichier NOT NULL
Projet_socialONG(#Projet_social=>Projet_social, ONG=>ONG)
Membre(#id: int, nom: varchar[20], naissance: Date, prenom: varchar[20], pays: varchar[10]) nom, naissance, prenom et pays NOT NULL
Avis(projet=>Projet, contributeur=>Contributeur, date: Date, note: int, texte: text) date, note et texte NOT NULL AND 1<=note<=5
MembreProjet(#projet=>Projet, membre=>Membre, rôle: {'chef de projet', 'développeur', 'designer', 'community manager'}) rôle NOT NULL 

Contraintes : 

Intersection(Projection(Contrepartie_physique, id), Projection(Contrepartie_numérique, id)) = {}
Intersection(Projection(Projet_social, id), Projection(Projet_techno, id), Projection(Projet_artis, id)) = {}
Intersection(Projection(Contributeur, id), Projection(Membre, id)) = {}
Le contributeur doit avoir contributé pour donner un avis
Projection(Membre, id) = Projection(MembreProjet, membre)