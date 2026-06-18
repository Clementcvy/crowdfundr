// Requete d'insertion des projets normalisés.
// 1. Depuis le dossier NoSQL/Application :
//    mongosh "mongodb://localhost:27017" 01_insertion_projets.js
// 2. Depuis mongosh, depuis le dossier NoSQL/Application :
//    load("01_insertion_projets.js")

conn = new Mongo("mongodb://localhost:27017");
db = conn.getDB("crowdfunder");

// ==========================================
// 1. Collection Contributeurs
// ==========================================
print("--- COLLECTION CONTRIBUTEURS ---");
db.Contributeurs.drop();

db.Contributeurs.insertMany([
   { "pseudo": "dupondt", "mail": "d@mail.com" },
   { "pseudo": "marty", "mail": "m@mail.com" },
   { "pseudo": "tipeu", "mail": "p@mail.com" },
   { "pseudo": "roy", "mail": "l@mail.com" },
   { "pseudo": "berny", "mail": "b@mail.com" }
]);

// ==========================================
// 2. Collection Membres
// ==========================================
print("\n--- COLLECTION MEMBRES ---");
db.Membres.drop();

db.Membres.insertMany([
   { "nom": "Durand", "prenom": "Marie" },
   { "nom": "Zola", "prenom": "Emile" },
   { "nom": "Smith", "prenom": "John" },
   { "nom": "Shinkawa", "prenom": "Yoji" },
   { "nom": "Kojima", "prenom": "Hideo" }
]);

// ==========================================
// Raccourcis de requêtes
// ==========================================
// Fonctions permettent de chercher l'_id pour l'injecter comme clé étrangère
function getMembreId(prenom, nom) {
    let membre = db.Membres.findOne({ "prenom": prenom, "nom": nom });
    return membre ? membre._id : null;
}

function getContributeurId(pseudo) {
    let contrib = db.Contributeurs.findOne({ "pseudo": pseudo });
    return contrib ? contrib._id : null;
}

// ==========================================
// 3. Collection Projets (Avec Références / ID)
// ==========================================
print("\n--- COLLECTION PROJETS ---");
db.Projets.drop();

print("Insertion des projets normalisés...");
let resProjets = db.Projets.insertMany([
   // ==========================================
   // PROJETS ARTISANAT (1 à 5)
   // ==========================================
   {
      "titre": "Tactical Art",
      "description": "Expo jeu video",
      "objectif": 1000.0,
      "lancement": "2026-01-01",
      "type": "Projet_Artis",
      "details_type": { "medium": "Jeu Video" },
      "incubateur": { "nom": "Le Cargo", "creation": 2016, "budget": 500000 },
      "membres": [
         { "membre_id": getMembreId("Hideo", "Kojima"), "role": "chef de projet" },
         { "membre_id": getMembreId("Yoji", "Shinkawa"), "role": "designer" }
      ],
      "contributions": [
         {
            "date": "2026-01-05T10:00:00Z",
            "montant": 600.0,
            "contributeur_id": getContributeurId("dupondt"),
            "contrepartie": { "type": "Numérique", "format": "PDF", "tailleFichier": 10 }
         },
         {
            "date": "2026-01-06T12:00:00Z",
            "montant": 500.0,
            "contributeur_id": getContributeurId("marty"),
            "contrepartie": { "type": "Numérique", "format": "MP3", "tailleFichier": 20 }
         },
         {
            "date": "2026-01-20T18:00:00Z",
            "montant": 60.0,
            "contributeur_id": getContributeurId("tipeu"),
            "contrepartie": {
               "type": "Physique", "poids": 4.0, "fraisLivraison": 20.0,
               "transporteur": { "nom": "Chronopost", "delai": 2 }
            }
         }
      ],
      "avis": [
         { "date": "2026-01-10", "note": 5, "texte": "Merveilleux", "contributeur_id": getContributeurId("dupondt") },
         { "date": "2026-01-15", "note": 5, "texte": "Incroyable", "contributeur_id": getContributeurId("marty") }
      ]
   },
   {
      "titre": "Artisanat 2",
      "description": "Peinture",
      "objectif": 2000.0,
      "lancement": "2026-01-02",
      "type": "Projet_Artis",
      "details_type": { "medium": "Peinture" },
      "incubateur": { "nom": "Station F", "creation": 2017, "budget": 1000000 },
      "membres": [
         { "membre_id": getMembreId("Marie", "Durand"), "role": "développeur" }
      ],
      "contributions": [
         {
            "date": "2026-01-10T16:00:00Z",
            "montant": 20.0,
            "contributeur_id": getContributeurId("roy"),
            "contrepartie": {
               "type": "Physique", "poids": 1.0, "fraisLivraison": 5.0,
               "transporteur": { "nom": "Chronopost", "delai": 2 }
            }
         }
      ],
      "avis": []
   },
   {
      "titre": "Artisanat 3",
      "description": "Sculpture",
      "objectif": 3000.0,
      "lancement": "2026-01-03",
      "type": "Projet_Artis",
      "details_type": { "medium": "Sculpture" },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("John", "Smith"), "role": "designer" }
      ],
      "contributions": [],
      "avis": []
   },
   {
      "titre": "Artisanat 4",
      "description": "Musique",
      "objectif": 4000.0,
      "lancement": "2026-01-04",
      "type": "Projet_Artis",
      "details_type": { "medium": "Musique" },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("Emile", "Zola"), "role": "community manager" }
      ],
      "contributions": [],
      "avis": []
   },
   {
      "titre": "Artisanat 5",
      "description": "Cinema",
      "objectif": 5000.0,
      "lancement": "2026-01-05",
      "type": "Projet_Artis",
      "details_type": { "medium": "Cinema" },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("Hideo", "Kojima"), "role": "chef de projet" }
      ],
      "contributions": [],
      "avis": []
   },

   // ==========================================
   // PROJETS SOCIAUX (6 à 10)
   // ==========================================
   {
      "titre": "Human Rights",
      "description": "Droits Humains",
      "objectif": 500.0,
      "lancement": "2026-02-01",
      "type": "Projet_Social",
      "details_type": {
         "region": "Monde",
         "ong": { "nom": "Amnesty Internat.", "pays": "Royaume-Uni" }
      },
      "incubateur": { "nom": "Techstars", "creation": 2006, "budget": 2000000 },
      "membres": [
         { "membre_id": getMembreId("Yoji", "Shinkawa"), "role": "designer" }
      ],
      "contributions": [
         {
            "date": "2026-02-05T09:00:00Z",
            "montant": 100.0,
            "contributeur_id": getContributeurId("berny"),
            "contrepartie": { "type": "Numérique", "format": "MP4", "tailleFichier": 30 }
         },
         {
            "date": "2026-02-06T14:00:00Z",
            "montant": 80.0,
            "contributeur_id": getContributeurId("tipeu"),
            "contrepartie": { "type": "Numérique", "format": "ZIP", "tailleFichier": 40 }
         },
         {
            "date": "2026-02-20T09:00:00Z",
            "montant": 70.0,
            "contributeur_id": getContributeurId("roy"),
            "contrepartie": {
               "type": "Physique", "poids": 5.0, "fraisLivraison": 25.0,
               "transporteur": { "nom": "Chronopost", "delai": 2 }
            }
         }
      ],
      "avis": [
         { "date": "2026-03-01", "note": 4, "texte": "Tres important", "contributeur_id": getContributeurId("berny") },
         { "date": "2026-04-01", "note": 5, "texte": "Bravo Amnesty", "contributeur_id": getContributeurId("tipeu") }
      ]
   },
   {
      "titre": "Social 2",
      "description": "Ecoles",
      "objectif": 600.0,
      "lancement": "2026-02-02",
      "type": "Projet_Social",
      "details_type": {
         "region": "Europe",
         "ong": { "nom": "Croix-Rouge", "pays": "France" }
      },
      "incubateur": { "nom": "Station F", "creation": 2017, "budget": 1000000 },
      "membres": [
         { "membre_id": getMembreId("Marie", "Durand"), "role": "développeur" }
      ],
      "contributions": [
         {
            "date": "2026-02-15T10:00:00Z",
            "montant": 30.0,
            "contributeur_id": getContributeurId("dupondt"),
            "contrepartie": { "type": "Numérique", "format": "RAR", "tailleFichier": 50 }
         }
      ],
      "avis": []
   },
   {
      "titre": "Social 3",
      "description": "Eau potable",
      "objectif": 700.0,
      "lancement": "2026-02-03",
      "type": "Projet_Social",
      "details_type": {
         "region": "Afrique",
         "ong": { "nom": "MSF", "pays": "Suisse" }
      },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("John", "Smith"), "role": "designer" }
      ],
      "contributions": [],
      "avis": []
   },
   {
      "titre": "Social 4",
      "description": "Agriculture",
      "objectif": 800.0,
      "lancement": "2026-02-04",
      "type": "Projet_Social",
      "details_type": {
         "region": "Asie",
         "ong": { "nom": "WWF", "pays": "Suisse" }
      },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("Emile", "Zola"), "role": "community manager" }
      ],
      "contributions": [],
      "avis": []
   },
   {
      "titre": "Social 5",
      "description": "Refuges",
      "objectif": 900.0,
      "lancement": "2026-02-05",
      "type": "Projet_Social",
      "details_type": {
         "region": "Amerique",
         "ong": { "nom": "Greenpeace", "pays": "Pays-Bas" }
      },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("Hideo", "Kojima"), "role": "chef de projet" }
      ],
      "contributions": [],
      "avis": []
   },

   // ==========================================
   // PROJETS TECHNO (11 à 15)
   // ==========================================
   {
      "titre": "Ocean Bot",
      "description": "Robot marin",
      "objectif": 10000.0,
      "lancement": "2026-03-01",
      "type": "Projet_Techno",
      "details_type": { "innovation": "Robotique" },
      "incubateur": { "nom": "Y Combinator", "creation": 2005, "budget": 5000000 },
      "membres": [
         { "membre_id": getMembreId("Yoji", "Shinkawa"), "role": "designer" }
      ],
      "contributions": [
         {
            "date": "2026-03-10T11:00:00Z",
            "montant": 40.0,
            "contributeur_id": getContributeurId("marty"),
            "contrepartie": {
               "type": "Physique", "poids": 2.0, "fraisLivraison": 10.0,
               "transporteur": { "nom": "Chronopost", "delai": 2 }
            }
         }
      ],
      "avis": [
         { "date": "2026-03-20", "note": 3, "texte": "Techno sympa", "contributeur_id": getContributeurId("marty") }
      ]
   },
   {
      "titre": "Tech 2",
      "description": "IA Medicale",
      "objectif": 20000.0,
      "lancement": "2026-03-02",
      "type": "Projet_Techno",
      "details_type": { "innovation": "IA" },
      "incubateur": { "nom": "Plug and Play", "creation": 2006, "budget": 1500000 },
      "membres": [
         { "membre_id": getMembreId("Marie", "Durand"), "role": "développeur" }
      ],
      "contributions": [
         {
            "date": "2026-03-15T14:00:00Z",
            "montant": 50.0,
            "contributeur_id": getContributeurId("berny"),
            "contrepartie": {
               "type": "Physique", "poids": 3.0, "fraisLivraison": 15.0,
               "transporteur": { "nom": "Chronopost", "delai": 2 }
            }
         }
      ],
      "avis": []
   },
   {
      "titre": "Tech 3",
      "description": "Blockchain",
      "objectif": 30000.0,
      "lancement": "2026-03-03",
      "type": "Projet_Techno",
      "details_type": { "innovation": "Web3" },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("John", "Smith"), "role": "designer" }
      ],
      "contributions": [],
      "avis": []
   },
   {
      "titre": "Tech 4",
      "description": "Energie solaire",
      "objectif": 40000.0,
      "lancement": "2026-03-04",
      "type": "Projet_Techno",
      "details_type": { "innovation": "Cleantech" },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("Emile", "Zola"), "role": "community manager" }
      ],
      "contributions": [],
      "avis": []
   },
   {
      "titre": "Tech 5",
      "description": "Domotique",
      "objectif": 50000.0,
      "lancement": "2026-03-05",
      "type": "Projet_Techno",
      "details_type": { "innovation": "IoT" },
      "incubateur": null,
      "membres": [
         { "membre_id": getMembreId("Marie", "Durand"), "role": "chef de projet" }
      ],
      "contributions": [],
      "avis": []
   }
]);

print("Insertion terminée.");

print("\n--- BILAN FINAL ---");
print("Nombre final de projets insérés       : " + db.Projets.countDocuments());
print("Nombre final de contributeurs insérés : " + db.Contributeurs.countDocuments());
print("Nombre final de membres insérés       : " + db.Membres.countDocuments());