var crowdFundrMongoUri = typeof process !== "undefined" && process.env && process.env.MONGODB_URI
   ? process.env.MONGODB_URI
   : "mongodb://localhost:27017";

conn = new Mongo(crowdFundrMongoUri);
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
