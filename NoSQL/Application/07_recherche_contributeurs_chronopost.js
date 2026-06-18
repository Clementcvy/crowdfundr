// Recherche 3 : utilisateurs distincts ayant reclame une contrepartie physique Chronopost.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 07_recherche_contributeurs_chronopost.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("07_recherche_contributeurs_chronopost.js")
// Pour chaque projet accompagne par un incubateur, affiche combien d'utilisateurs
// distincts ont reclame au moins une contrepartie physique expediee par Chronopost.

conn = new Mongo("mongodb://localhost:27017");
db = conn.getDB("crowdfunder");
load("outils.js")

print("Recherche 3 : nombre d'utilisateurs distincts par projet avec incubateur ayant reclame une contrepartie physique expediee par Chronopost");

db.Projets.aggregate([
   // 1. On garde seulement les projets qui ont un incubateur
   {
      $match: {
         incubateur: { $ne: null }
      }
   },

   // 2. On deplie les contributions
   {
      $unwind: "$contributions"
   },

   // 3. On garde seulement les contributions avec une contrepartie physique
   //    expediee par Chronopost
   {
      $match: {
         "contributions.contrepartie.type": "Physique",
         "contributions.contrepartie.transporteur.nom": "Chronopost"
      }
   },

   // 4. On regroupe par projet
   //    et on stocke les contributeurs sans doublon
   {
      $group: {
         _id: "$_id",
         titre: { $first: "$titre" },
         contributeurs: {
            $addToSet: "$contributions.contributeur.pseudo"
         }
      }
   },

   // 5. On affiche le projet et le nombre de contributeurs distincts
   {
      $project: {
         _id: 0,
         projet: "$titre",
         nb_contributeurs: { $size: "$contributeurs" }
      }
   }
]).forEach(printjson);
