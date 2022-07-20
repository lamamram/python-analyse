BEGIN;
PRAGMA encoding="UTF-8";
DROP TABLE IF EXISTS `domain_name`;
CREATE TABLE `domain_name` (
    `dns_id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `iso2` CHAR(2) NOT NULL,
    `name` VARCHAR(100) DEFAULT NULL,
	`created_at` TEXT DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS `pays`;
CREATE TABLE `pays` (
    `iso2` char(2) PRIMARY KEY,
    `name` varchar(100) DEFAULT NULL
);

INSERT INTO `pays` VALUES ('AE','Emirats Arabes Unis'),('AT','Autriche'),('AU','Australie'),('BE','Belgique'),('BS','Bahamas'),('CA','Canada'),('CH','Chine'),('CY','Chypre'),('CZ','République tchèque'),('DE','Allemagne'),('DK','Danemark'),('ES','Espagne'),('FR','France'),('GB','Royaume Uni'),('GP','Guadeloupe'),('HK','Hong Kong'),('IE','Irlande'),('IL','Israël'),('IT','Italie'),('JP','Japon'),('KR','République de Corée'),('KY','Iles Caïmans'),('LI','Liechtenstein'),('LU','Luxembourg'),('MA','Maroc'),('MC','Monaco'),('MQ','Martinique'),('MU','Maurice'),('NL','Pays-Bas'),('NO','Norvège'),('PM','Saint-Pierre et Miquelon'),('RE','Réunion'),('SE','Suède'),('SG','Singapour'),('US','Etats Unis');
COMMIT;