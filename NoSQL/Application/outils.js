function getMembreId(prenom, nom) {
   let membre = db.Membres.findOne({ "prenom": prenom, "nom": nom });
   return membre ? membre._id : null;
}

function getContributeurId(pseudo) {
   let contrib = db.Contributeurs.findOne({ "pseudo": pseudo });
   return contrib ? contrib._id : null;
}

function getMembre(id) {
   let membre = db.Membres.findOne(id);
   return membre;
}

function getContributeur(id) {
   let contrib = db.Contributeurs.findOne(id);
   return contrib;
}