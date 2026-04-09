# Plateforme de financement participatif CrowdFundr



## 1. Description



CrowdFundr, une plateforme moderne de financement participatif, souhaite concevoir une base de données pour gérer les projets proposés, les équipes de créateurs, les soutiens financiers et ses utilisateurs.


## 2. Données à traiter 


Projet : titre, description, objectif financier (€), date de lancement, incubateur (optionnel)
* Projet Artistique : medium
* Projet Social : région
* Projet Technologique : innnovation 

Membre d'équipe : nom, prénom, pays de résidence, date de naissance, rôle

Rôle (énumération): { chef de projet, développeur, designer, community manager }

Membre Projet : role

Incubateur : nom, année de création, budget d'accompagnement.

Utilisateur (Contributeur) : pseudo unique, email, nom, date de naissance.

ONG : n° enregistrement unique, nom, pays d'origine.

Transporteur : nom, délai moyen (jours).

Avis : date, note, texte

Contributeurs :  pseudo , mail ,nom , naissance

Contribution : date, montant

Contrepartie :
*Contrepartie Numérique : format, taille fichier
*Contrepartie Physique : poids, frais de livraison  

## 3. Contraintes:

* Un Projet a au moins un Membre.
* Pour donner un Avis, un Membre doit avoir contribué au Projet.
* Chaque Membre a un Rôle unique sur ce Projet. 
* Une Contrepartie physique à un unique Transporteur.
* Un Projet à au plus un Incubateur.
* Un Contributeur ne peut donner qu'un seul avis.  
* Les notes vont de 1 à 5.
* Une Contribution est forcément liée à une Contrainte et un Projet.



## 4. Hypothèses:

* Des instances des classes Contributeur, ONG, Incubateur, Membre peuvent exister sans intéragir avec d'autres classes de la base.  
* On part du principe qu'il existe une relation de composition entre la Contrepartie (composant) et la Contribution (composite) puisque certaines Contributions ont une Contrepartie et toute Contrepartie n'existe que dans le contexte d'une Contribution.
* La classe Projet est abstraite car un projet est forcément artistique, technologique ou social.
* La classe Contrepartie est une interface car une contrepartie est forcément physique ou numérique et ces deux types n'ont aucun attribut en commun.
* On définit la classe Rôle comme énumération car le sujet mentionne un nombre fini de rôles.
* Les classes Avis, Contribution et MembreProjet sont définies comme des classes d'association car elle permettent d'ajouter des propriétés à des associations entre d'autres classes.
* L'attribut date de Contribution est une clé pour matérialiser le fait qu'un Membre puisse contribuer plusieurs fois à un même Projet.


## 5. Objet 

Nous allons creer une base de données pour aider la plateforme CrowdFunder puisse savoir:- quels projet artistiques font intervenir à la fois Hideo Kojima et Yona Shinkawa et ont dépassé leur objectif financier 

-La moyenne dee notes des projets sociaux qui sont soutenus par l'ONG nommée Amnesty International, en ne prenant en compte que les utilisateurs ayant apporté une contribution supérieure à 50 euros sur ces projets 

-Combien d'utilisateurs distincts ont réclamé au moins une contrepartie physique expédiée via le transporteur "Chronopost" lors de leurs contributions ,pour chaque projet accompagné par un incubateur 



## 6. Livrables 

-MCD v1 ,v2

-MLD v1,v2

-SQL (LDD,LMD)

-L'application en python 

-No SQL

-Étude de la normalisation 

## 7. Organisation du travail : 

### Utilisation IA:

| rendu  | oui/non| prompt |
| ------ | ------ | ------ |
| UML1 |oui|réarrangement PlantUML (esthétique)|
|        |        |        |

### Participation :

| rendu  | Hugo   | Mathis | Tom    | Clement|
| ------ | ------ | ------ | ------ | ------ |
| NDC/UML1 |   25%   |   25%   |   25%   |   25%   |
|        |        |        |        |        |
|        |        |        |        |        |
|        |        |        |        |        |
|Pourcentage totale:|        |        |        |        |





