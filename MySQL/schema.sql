CREATE SCHEMA `cpsc408_2295968`;

CREATE TABLE IF NOT EXISTS cpsc408_2295968.`Usage` (
	usageID INT NOT NULL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS cpsc408_2295968.Effect (
	effectID INT NOT NULL PRIMARY KEY,
	parentUsage INT,
	save VARCHAR(20),
	damage VARCHAR(8),
	txt VARCHAR(200),
    FOREIGN KEY (parentUsage) REFERENCES `Usage`(usageID)
);

CREATE TABLE IF NOT EXISTS cpsc408_2295968.Spell (
	spellID INT NOT NULL PRIMARY KEY,
	name VARCHAR(100),
	level INT,
	school VARCHAR(15),
	castingTime VARCHAR(15),
	`range` INT,
	target VARCHAR(25),
	hasVerbal TINYINT(1),
	hasSomatic TINYINT(1),
	materialComponents VARCHAR(200),
	concentration TINYINT(1),
	duration INT,
	primaryEffect INT,
	secondaryEffect INT,
	FOREIGN KEY (primaryEffect) REFERENCES Effect(effectID),
	FOREIGN KEY (secondaryEffect) REFERENCES Effect(effectID)
);

CREATE TABLE IF NOT EXISTS cpsc408_2295968.Class (
	classID INT NOT NULL PRIMARY KEY,
	name VARCHAR(100),
	castingMod VARCHAR(20),
	halfCast TINYINT(1),
	hitDie VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS cpsc408_2295968.Background (
	backgroundID INT NOT NULL PRIMARY KEY,
	name VARCHAR(70)
);

CREATE TABLE IF NOT EXISTS cpsc408_2295968.`Character` (
	characterID INT NOT NULL PRIMARY KEY,
	name VARCHAR(70),
	background INT,
	class INT,
	level INT,
	secondClass INT,
	secondLevel INT,
	thirdClass INT,
	thirdLevel INT,
	fourthClass INT,
	fourthLevel INT,
	FOREIGN KEY (background) REFERENCES Background(backgroundID),
	FOREIGN KEY (class) REFERENCES Class(ClassID),
	FOREIGN KEY (secondClass) REFERENCES Class(ClassID),
	FOREIGN KEY (thirdClass) REFERENCES Class(ClassID),
	FOREIGN KEY (fourthClass) REFERENCES Class(ClassID)
);

CREATE TABLE IF NOT EXISTS cpsc408_2295968.ClassSpell (
	classID INT NOT NULL,
	spellID INT NOT NULL,
	PRIMARY KEY (classID, spellID),
	FOREIGN KEY (classID) REFERENCES Class(classID),
	FOREIGN KEY (spellID) REFERENCES Spell(spellID)
);

Delimiter //
CREATE TRIGGER `cpsc408_2295968`.BefDelEffect BEFORE DELETE ON cpsc408_2295968.`Effect`
FOR EACH ROW BEGIN
UPDATE cpsc408_2295968.`Spell` SET primaryEffect=0 WHERE OLD.effectID=primaryEffect;
UPDATE cpsc408_2295968.`Spell` SET secondaryEffect=0 WHERE OLD.effectID=secondaryEffect;
END;
//
Delimiter ;

CREATE TRIGGER `cpsc408_2295968`.DelUsage BEFORE DELETE ON cpsc408_2295968.`Usage`
FOR EACH ROW
UPDATE cpsc408_2295968.`Effect` SET parentUsage=0 WHERE OLD.usageID=parentUsage;

CREATE TRIGGER `cpsc408_2295968`.DelSpell BEFORE DELETE ON cpsc408_2295968.`Spell`
FOR EACH ROW
DELETE FROM cpsc408_2295968.`ClassSpell` WHERE OLD.spellID=ClassSpell.spellID;

CREATE TRIGGER `cpsc408_2295968`.DelBackground BEFORE DELETE ON cpsc408_2295968.`Background`
FOR EACH ROW
DELETE FROM cpsc408_2295968.`Character` WHERE OLD.backgroundID=background;

Delimiter //
CREATE TRIGGER `cpsc408_2295968`.DelClass BEFORE DELETE ON cpsc408_2295968.`Class`
FOR EACH ROW BEGIN
DELETE FROM cpsc408_2295968.`ClassSpell` WHERE OLD.classID=ClassSpell.classID;
UPDATE cpsc408_2295968.`Character` SET class=0 WHERE OLD.classID=class;
UPDATE cpsc408_2295968.`Character` SET secondClass=0 WHERE OLD.classID=secondClass;
UPDATE cpsc408_2295968.`Character` SET thirdClass=0 WHERE OLD.classID=thirdClass;
UPDATE cpsc408_2295968.`Character` SET fourthClass=0 WHERE OLD.classID=fourthClass;
END;
//
Delimiter ;



USE `cpsc408_2295968`;

INSERT INTO `Usage` VALUES(0,'NULL USAGE');
INSERT INTO `Effect` VALUES(0,0,'NULL','NULL','NULL');
INSERT INTO `Spell` VALUES(0,'NULL SPELL',0,'NULL','NULL',0,'NULL',0,0,'NULL',0,0,0,0);
INSERT INTO `Class` VALUES(0,'NULL CLASS','NULL',0,0);
INSERT INTO `Background` VALUES(0,'NULL BACKGROUND');
INSERT INTO `Character` VALUES(0, 'NULL CHARACTER',0,0,0,0,0,0,0,0,0);