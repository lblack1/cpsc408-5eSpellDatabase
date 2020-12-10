USE `cpsc408_2295968`;
LOAD DATA INFILE '/var/lib/mysql-files/infileUsage.txt' INTO TABLE `Usage` FIELDS TERMINATED BY ',';
LOAD DATA INFILE '/var/lib/mysql-files/infileEffect.txt' INTO TABLE `Effect` FIELDS TERMINATED BY ',';
LOAD DATA INFILE '/var/lib/mysql-files/infileSpell.txt' INTO TABLE `Spell` FIELDS TERMINATED BY ',';
LOAD DATA INFILE '/var/lib/mysql-files/infileClass.txt' INTO TABLE `Class` FIELDS TERMINATED BY ',';
LOAD DATA INFILE '/var/lib/mysql-files/infileBackground.txt' INTO TABLE `Background` FIELDS TERMINATED BY ',';
LOAD DATA INFILE '/var/lib/mysql-files/infileCharacter.txt' INTO TABLE `Character` FIELDS TERMINATED BY ',';
LOAD DATA INFILE '/var/lib/mysql-files/infileClassSpell.txt' IGNORE INTO TABLE `ClassSpell` FIELDS TERMINATED BY ',';
