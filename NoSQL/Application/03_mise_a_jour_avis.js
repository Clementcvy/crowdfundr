// Requete de mise a jour d'un avis.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 03_mise_a_jour_avis.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("03_mise_a_jour_avis.js")
// Utilise $set pour modifier la note de dupondt sur le projet Tactical Art.

try {
   load("bootstrap.js");
} catch (erreur) {
   try {
      load("NoSQL/Application/bootstrap.js");
   } catch (autreErreur) {
      load("/scripts/bootstrap.js");
   }
}

contID = getContributeurId("dupondt");

print("Mise a jour de la note de dupondt sur Tactical Art");
contID = getContributeurId("dupondt");

print("Avant modification : avis du projet Tactical Art");
printjson(db.Projets.findOne(
   { titre: "Tactical Art" },
   { titre: 1, avis: 1 }
));

resultat = db.Projets.updateOne(
   {
      titre: "Tactical Art",
      "avis.contributeur_id": contID
   },
   {
      $set: {
         "avis.$.note": 2
      }
   }
);

print("Resultat de la modification");
printjson(resultat);

print("Apres modification : avis du projet Tactical Art");
printjson(db.Projets.findOne(
   { titre: "Tactical Art" },
   { titre: 1, avis: 1 }
));
