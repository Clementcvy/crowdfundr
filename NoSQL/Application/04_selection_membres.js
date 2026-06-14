// Requete de selection des membres d'un projet.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 04_selection_membres.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("04_selection_membres.js")
// Affiche les membres du projet Tactical Art.

conn = new Mongo("mongodb://localhost:27017");
db = conn.getDB("crowdfunder");

print("Selection des membres du projet Tactical Art");

recordset = db.Projets.find(
   { titre: "Tactical Art" },
   {
      membres: 1
   }
);

while (recordset.hasNext()) {
   printjson(recordset.next());
}
