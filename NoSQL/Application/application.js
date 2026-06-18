// Execution de toutes les requetes, dans l'ordre :
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" application.js
// 2. Depuis la racine du projet :
//    mongosh "mongodb://localhost:27017" NoSQL/Application/application.js
// 3. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("application.js")

print("Execution de toutes les requetes");

function chargerRequete(fichier) {
   try {
      load(fichier);
   } catch (erreur) {
      if (String(erreur.message).indexOf("ENOENT") === -1) {
         throw erreur;
      }

      load("NoSQL/Application/" + fichier);
   }
}
chargerRequete("01_insertion_projets.js");
chargerRequete("02_suppression_avis.js");
chargerRequete("03_mise_a_jour_avis.js");
chargerRequete("04_selection_membres.js");
chargerRequete("05_recherche_projets_artisanaux_finances.js");
chargerRequete("06_recherche_moyenne_avis_ong.js");
chargerRequete("07_recherche_contributeurs_chronopost.js");
