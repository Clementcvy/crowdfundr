// Requete de selection des membres d'un projet.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 04_selection_membres.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("04_selection_membres.js")
// Affiche les membres du projet Tactical Art.

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

print("Selection des membres du projet Tactical Art");

recordset = db.Projets.findOne(
   { titre: "Tactical Art" },
   {
      membres: 1
   }
);

for (const doc of recordset.membres) {
   membre = getMembre(doc.membre_id);
   printjson(membre);
}


