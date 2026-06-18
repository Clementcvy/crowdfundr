// Recherche 1 : projets artisanaux finances avec Kojima Hideo et Shinkawa Yoji.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 05_recherche_projets_artisanaux_finances.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("05_recherche_projets_artisanaux_finances.js")
// Affiche les projets artisanaux dont la somme des contributions atteint l'objectif.

conn = new Mongo("mongodb://localhost:27017");
db = conn.getDB("crowdfunder");
load("outils.js")

print("Recherche 1 : projets artisanaux finances");

membreID = getMembreId("Hideo", "Kojima");
membreID2 = getMembreId("Yoji", "Shinkawa");

db.Projets.aggregate([
   {
      // 1. On garde seulement les projets artisanaux
      $match: {
         type: "Projet_Artis",
         // 2. On verifie que les deux membres sont dans le projet
         membres: {
            $all: [
               { $elemMatch: { membre_id: membreID } },
               { $elemMatch: { membre_id: membreID2 } }
            ]
         }
      }
   },
   {
      // 3. On garde seulement les projets finances
      $match: {
         $expr: {
            $gte: [{ $sum: "$contributions.montant" }, "$objectif"]
         }
      }
   }
]).forEach(printjson);
