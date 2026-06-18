// Requete de suppression d'un avis.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 02_suppression_avis.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("02_suppression_avis.js")
// Utilise $pull pour supprimer l'avis de marty du projet Tactical Art.

conn = new Mongo("mongodb://localhost:27017");
db = conn.getDB("crowdfunder");

load("outils.js")

print("Suppression de l'avis de marty sur Tactical Art");

print("Avant modification : avis du projet Tactical Art");
printjson(db.Projets.findOne(
   { titre: "Tactical Art" },
   { titre: 1, avis: 1 }
));

resultat = db.Projets.updateOne(
   { titre: "Tactical Art" },
   { $pull: { avis: { contributeur: "marty" } } }
);

print("Resultat de la modification");
printjson(resultat);

print("Apres modification : avis du projet Tactical Art");
printjson(db.Projets.findOne(
   { titre: "Tactical Art" },
   { titre: 1, avis: 1 }
));
