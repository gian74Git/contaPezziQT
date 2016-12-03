CREATE TABLE "TLet_Letture" (
  "iLetId" INTEGER PRIMARY KEY AUTOINCREMENT,
  "sLetNote" VARCHAR NOT NULL,
  "dLetDataLettura" date NOT NULL DEFAULT '0000-00-00',
  "tLetOraIni" time NOT NULL,
  "tLetOraFine" time NOT NULL,
  "iLetNumProg" INTEGER NOT NULL
) 
