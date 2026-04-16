Choix de modélisation : 

On modélise Contrepartie avec un héritage par référence, car ce n’est pas un héritage semi-complet et on a une association complexe sur la mère.
On modélise Personne avec un héritage par les classes filles, car c’est une classe abstraite et on a pas d’association sur la mère.
On modélise Projet avec un héritage par référence, car ce n’est pas un héritage semi-complet et on a une association complexe sur la mère.

Relations : 
Incubateur (#nom : varchar[20], création :integer[4] , budget : float)
ONG (#NEU : integer , nom : varchar[20], pays : varchar[20] )
Transporteur (#nom : varchar [20], delai : integer)
Membre (#id: int, nom : varchar [20], prenom : varchar[20], naissance : date , pays : varchar [10]) 
Projet_Techno(#titre=>Projet, ,#lancement : date =>Projet ,innovation :text)
Projet_Artis(#titre=>Projet, #lancement=>Projet, médium: text)
Projet_Social(#titre=>Projet, #lancement=>Projet, région: text)
Projet_socialONG(#titre_projet=>Projet_Social, lancement_projet=>Projet_Social, NEU=>ONG)
Contrepartie(#id : int, contribution => Contribution) contribution NOT NULL
Contrepartie_Numérique(#id => Contrepartie, format : varchar[10], tailleFichier: int)
Contrepartie_Physique(#id => Contrepartie, poids : float, fraisLivraison: int, transporteur => Transporteur) transporteur NOT NULL
Contribution(#date: DateTime, montant: float, projet_titre=>Projet, projet_lancement=>Projet, contributeur=>Contributeur), projet_titre NOT NULL AND projet_lancement NOT NULL
Contributeur(#id: int, pseudo: varchar[20], mail: varchar[20], nom: varchar[20], naissance: Date) pseudo KEY
Projet(#titre: varchar[20], description: text, objectif: float, #lancement: Date, incubateur => Incubateur, contributeur=>Contributeur, date_avis: Date, note_avis: int[1..5], texte_avis: text)

MembreProjet ( rôle: {chef de projet, développeur, designer, community manager} ,nom_membre=>membre , prenom_membre=>membre , naissance_membre=>membre titre_projet=> projet ,lancement_projet=> projet )nom_membre NOT NULL AND prenom_membre NOT NULL AND naissance_membre NOT NULL 



Contraintes : 
Intersection(Projection(Contrepartie_Numérique, id), Projection(Contrepartie_Physique, id)) = {}
Projection(Contrepartie, id) = Projection(Contrepartie_Physique, id)) UNION Projection(Contrepartie_Physique, id)
Intersection(Projection(Projet_Techno, titre, lancement), Projection(Projet_Artis, titre, lancement), Projection(Projet_Social, titre, lancement)) = {}
Projection(Projet, titre, lancement) = Projection(Projet_Techno, titre, lancement)) UNION Projection(Projet_Artis, titre, lancement) UNION Projection(Projet_Social, titre, lancement))
Le contributeur doit avoir contribué pour donner un avis
Intersection(Projection(Membre, id), Projection(Contributeur, id)) = {}

