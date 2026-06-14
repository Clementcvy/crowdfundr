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
|        |        |        |
| MLDv2/LDD | oui | idées de SELECT |
|        |        |        |
| APP | oui |   | 
|        |        |        |
| NoSQL | non |   |
|        |        |        |
| APP NoSQL | non |   |


Prompt APP : [CODE] Pour ces menu, ajoute un retour en arrière pour chaque étape du menu avec des boucles. N'ajoute aucun commentaire et donne moi le fichier en entier. Ne touche pas les fonction. Et reste cohérent avec tes méthodes d'input pour le retour Python


### Participation :

| rendu  | Hugo   | Mathis | Tom    | Clement|
| ------ | ------ | ------ | ------ | ------ |
| NDC/UMLv1 |   25%   |   25%   |   25%   |   25%   |
|        |        |        |        |        |
|     UMLv2/MLD   |    25%    |   25%     |   25%     |   25%     |
|        |        |        |        |        |
|     MLDv2/LDD   |    25%    |   25%     |   25%     |   25%     |
|        |        |        |        |        |
|     APP   |    25%    |   25%     |   25%     |   25%     |
|        |        |        |        |        |
|     NoSQL   |    25%    |   25%     |   25%     |   25%     |
|        |        |        |        |        |
|     App NoSQL   |    22%    |   22%     |   22%     |   34%     |
|        |        |        |        |        |
| Pourcentage totale:|        |        |        |        |



## 8. Choix des classes à transformer en document JSON : 

**Projet_Techno** est modélisé comme un `DataType` car il ne représente pas une entité indépendante, mais un complément d’information propre à un projet de type technologique. Son attribut `innovation` vient enrichir le document `Projet`.

**Projet_Artis** est modélisé comme un `DataType` car il contient uniquement des informations spécifiques à un projet artistique, comme le `médium`. Ces données sont directement dépendantes du projet principal et n’ont pas besoin d’exister séparément.

**Projet_Social** est modélisé comme un `DataType` car il décrit les caractéristiques propres à un projet social, notamment la `région` et l’`ONG` associée. Il sert donc à spécialiser le document `Projet` sans créer une collection indépendante.

**ONG** est modélisée comme un `DataType` car elle est utilisée comme information descriptive dans un projet social. Elle peut être intégrée directement dans le document JSON du projet afin d’éviter une jointure supplémentaire.

**Membre** est modélisé comme un `DataType` car il correspond à une information incluse dans un projet, avec un prénom, un pays et un rôle. Les membres sont donc naturellement stockés sous forme de tableau imbriqué dans le document `Projet`.

**Contributeur** est modélisé comme un `DataType` car il sert principalement à identifier la personne qui effectue une contribution, avec un pseudo et une adresse mail. Ces informations peuvent être intégrées directement dans la contribution sans nécessiter une table ou collection séparée.

**Avis** est modélisé comme un `DataType` car il est fortement lié au projet concerné. Sa date, sa note et son texte peuvent être stockés directement dans le document `Projet`, par exemple dans un tableau d’avis.

**Transporteur** est modélisé comme un `DataType` car il décrit simplement les informations nécessaires à une contrepartie physique, comme le nom du transporteur et le délai. Il peut donc être imbriqué dans la contrepartie physique sans être géré séparément.

Les autres classes restent modélisées en SQL car elles représentent des entités principales du système, avec une identité propre, des clés et des relations importantes à maintenir. Par exemple, `Projet`, `Incubateur`, `Contribution`, `Contrepartie` ou encore `Rôle` nécessitent une gestion structurée et des contraintes d’intégrité fortes. De plus, certaines de ces classes manipulent des données sensibles ou transactionnelles, comme les montants des contributions, les budgets ou les contreparties associées aux paiements. Le modèle relationnel est donc plus adapté, car il permet de garantir la cohérence des données, d’éviter les pertes d’information, de sécuriser les opérations critiques et de bénéficier des propriétés transactionnelles du SQL.

## 9. BDD MongoDB

La base de données NoSQL a été implémentée avec MongoDB et des scripts JavaScript exécutables avec `mongosh`. Les données sont stockées dans la base `crowdfunder`, principalement dans la collection `Projets`, où chaque document regroupe les informations du projet ainsi que ses membres, contributions, contreparties, avis et éventuel incubateur.

Les scripts se trouvent dans le dossier `NoSQL/Application`. Le fichier `application.js` permet d'exécuter l'ensemble des requêtes dans l'ordre. Il commence par réinitialiser la collection `Projets`, puis insère les données d'exemple avant de lancer les requêtes de modification et de recherche.

Depuis la racine du projet, l'exécution complète se fait avec :

```bash
mongosh "mongodb://localhost:27017" NoSQL/Application/application.js
```

Chaque requête peut aussi être exécutée séparément. La commande à utiliser est indiquée en commentaire en haut de chaque fichier. Par exemple :

```bash
mongosh "mongodb://localhost:27017" NoSQL/Application/05_recherche_projets_artisanaux_finances.js
```

Les scripts de modification affichent l'état des données avant et après l'opération afin de montrer clairement l'effet de la requête exécutée.


