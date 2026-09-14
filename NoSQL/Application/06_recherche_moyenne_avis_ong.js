// Recherche 2 : moyenne des avis pour les contributeurs importants d'une ONG.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 06_recherche_moyenne_avis_ong.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("06_recherche_moyenne_avis_ong.js")
// Affiche la moyenne des notes pour Amnesty International avec contributions superieures a 50.

conn = new Mongo("mongodb://localhost:27017");
db = conn.getDB("crowdfunder");
try {
   load("outils.js");
} catch (erreur) {
   try {
      load("NoSQL/Application/outils.js");
   } catch (autreErreur) {
      load("/scripts/outils.js");
   }
}

print("Recherche 2 : moyenne des avis pour Amnesty International");

db.Projets.aggregate([
   // 1. On garde seulement les projets sociaux de l'ONG voulue
   {
      $match: {
         type: "Projet_Social",
         "details_type.ong.nom": "Amnesty Internat."
      }
   },

   // 2. On deplie les avis
   {
      $unwind: "$avis"
   },

   // 3. On deplie les contributions
   {
      $unwind: "$contributions"
   },

   // 4. On garde seulement les contributions du meme contributeur que l'avis
   //    et avec un montant superieur a 50
   {
      $match: {
         $expr: {
            $and: [
               { $eq: ["$avis.contributeur_id", "$contributions.contributeur_id"] },
               { $gt: ["$contributions.montant", 50] }
            ]
         }
      }
   },

   // 5. On calcule la moyenne des notes
   {
      $group: {
         _id: null,
         moyenneNote: { $avg: "$avis.note" }
      }
   },

   // 6. On affiche seulement la moyenne
   {
      $project: {
         _id: 0,
         moyenneNote: 1
      }
   }
]).forEach(printjson);
