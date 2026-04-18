# Plateforme de financement participatif CrowdFundr



## 1. Description



CrowdFundr, une plateforme moderne de financement participatif, souhaite concevoir une base de données pour gérer les projets proposés, les équipes de créateurs, les soutiens financiers et ses utilisateurs.


## 2. Données à traiter 


Projet : titre, description, objectif financier (€), date de lancement, incubateur (optionnel)
* Projet Artistique : medium
* Projet Social : région
* Projet Technologique : innovation 

Personne : nom, date de naissance
* Membre d'équipe : prénom, pays de résidence
* Contributeur :  pseudo , mail

Rôle (énumération): { chef de projet, développeur, designer, community manager }

Membre Projet : rôle

Incubateur : nom, année de création, budget d'accompagnement.

ONG : n° enregistrement unique, nom, pays d'origine.

Transporteur : nom, délai moyen (jours).

Avis : date, note, texte

Contribution : date-heure, montant

Contrepartie :
* Contrepartie Numérique : format, taille du fichier
* Contrepartie Physique : poids, frais de livraison  

## 3. Contraintes:

* Un Projet a au moins un Membre.
* Pour donner un Avis, un Contributeur doit avoir contribué au Projet.
* Pour un couple (Membre, Projet), un seul rôle est associé. 
* Une contrepartie numérique n'a pas de transporteur.
* Une contrepartie physique en a exactement un.
* Un Projet a au plus un Incubateur.
* Pour un couple (Contributeur, Projet), au plus un avis est autorisé.  
* Les notes vont de 1 à 5.
* Une Contribution est forcément liée à un Contributeur et à un Projet.
* Seuls les projets sociaux peuvent être soutenus par des ONG.
* Un Projet social peut être soutenu par des ONG.



## 4. Hypothèses:

* Des instances des classes Contributeur, ONG, Incubateur et Membre peuvent exister sans interagir avec d'autres classes de la base.  
* On part du principe qu'il existe une relation de composition entre la Contrepartie et la Contribution : une Contribution peut avoir une Contrepartie. On suppose que la contrepartie n'existe pas indépendamment.
* La classe Projet est abstraite car un projet est forcément artistique, technologique ou social. Il s'agit d'un héritage total et exclusif.
* La classe Contrepartie est une classe Abstraite car une contrepartie est forcément physique ou numérique. Il s'agit d'un héritage total et exclusif.
* On définit la classe Rôle comme énumération car le sujet mentionne un nombre fini de rôles.
* Les classes Avis et MembreProjet sont définies comme des classes d'association car elles permettent d'ajouter des propriétés à des associations entre d'autres classes.
* La date-heure permet la multiplicité des contributions entre un même contributeur et un même projet.
* On transforme l'héritage de Contrepartie par référence, car Contrepartie a une association complexe avec contribution
* On transforme l'héritage de Projet par référence, car l'héritage n'est pas semi-complet et il y a des associations complexes sur Projet
* On transforme l'héritage de Personne par les classes fille, car Personne est abstrait et n'a pas d'association


## 5. Objet 

Nous allons créer une base de données pour aider la plateforme CrowdFundr puisse savoir : quels projets artistiques font intervenir à la fois Hideo Kojima et Yoji Shinkawa et ont dépassé leur objectif financier 

-La moyenne des notes des projets sociaux qui sont soutenus par l'ONG nommée Amnesty International, en ne prenant en compte que les utilisateurs ayant apporté une contribution supérieure à 50 euros sur ces projets 

-Combien d'utilisateurs distincts ont réclamé au moins une contrepartie physique expédiée via le transporteur "Chronopost" lors de leurs contributions, pour chaque projet accompagné par un incubateur 



## 6. Livrables 

- MCD v1 ,v2

- MLD v1,v2

- SQL (LDD,LMD)

- L'application en python 

- NoSQL

- Étude de la normalisation 

## 7. Organisation du travail : 

### Utilisation IA:

| rendu  | oui/non | prompt |
| ------ | ------ | ------ |
| UMLv1 | oui | réarrangement PlantUML (esthétique) |
|        |        |        |
| UMLv2/MLD | oui | réarrangement PlantUML (esthétique) |



### Participation :

| rendu  | Hugo   | Mathis | Tom    | Clement|
| ------ | ------ | ------ | ------ | ------ |
| NDC/UMLv1 |   25%   |   25%   |   25%   |   25%   |
|        |        |        |        |        |
|     UMLv2/MLD   |    33%    |   33%     |        |   33%     |
|        |        |        |        |        |
| Pourcentage totale:|        |        |        |        |





