# Entry Generator for Lloyd's 5e Spell database

import random as r

r.seed()

#
# Usages
#

# IDs increment from 1
usagenames = []
with open("txtfiles/verbs.txt") as f:
	lines = f.readlines()
	for line in lines:
		usagenames.append(line.lstrip(" ").rstrip("\n"))

#childEffects start @ 0


#
# Effects
#

#IDs increment from 1
# parentUsgae random between 2 and 49,000
saves = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma", "None"]
dice = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
texts = []
with open("txtfiles/Latin-Lipsum.txt") as f:
	lines = f.readlines()
	for line in lines:
		texts.extend(line.strip(" .\n").split())


#
# Spells
#

# IDs increment from 1
spellnames = [["Tashas","Mordenkainens", "Xanathars", "Korfels", "Lloyds", "Volos", "Calebs", "Parths", "Thordaks", "Pumats", "Yussas", "Iouns", "Bahamuts", "Khysas", "Tavishas", "Gustavos", "Adrians", "Jons", "Kais", "Andrews"], [], []]
with open("txtfiles/RandomSpells.txt") as f:
	lines = f.readlines()
	for line in lines:
		spellnames[1].append(line.lstrip(" ").rstrip("\n"))

with open("txtfiles/RandomSpells2.txt") as f:
	lines = f.readlines()
	for line in lines:
		spellnames[2].append(line.lstrip(" ").rstrip("\n"))

schools = ["Transmutation", "Divination", "Abjuration", "Conjuration", "Illusion", "Evocation", "Necromancy", "Enchantment"]
castingtimes = ["1 action", "1 bonus action", "1 reaction", "1 minute", "10 minutes", "1 hour", "8 hours"]
#range between -1 and 5280
targets = ["1 creature", "1 target", "multiple creatures", "multiple targets"]
#hasVerbal is true or false
#hasSomatic is true or false
materialcomponents = []
with open("txtfiles/MaterialComponents.txt") as f:
	lines = f.readlines()
	for line in lines:
		materialcomponents.append(line.lstrip(" ").rstrip("\n"))

#concentration t or f
#duration between -1 and 600
#primaryeffect random between 1 and 1,000,000
#secondaryeffect random between 1 and 1,000,000


#
# Class
#

# IDs
classnames = [["Way of", "School of", "Path of", "Oath of", "Creed of", "Training of", "Mastery of", "College of", "Domain of", "Circle of"], [], ["Monk", "Wizard", "Paladin", "Barbarian", "Bard", "Ranger", "Cleric", "Fighter", "Druid", "Artificer", "Sorcerer", "Warlock", "Rogue"]]
with open("txtfiles/MaterialComponents.txt") as f:
	lines = f.readlines()
	for line in lines:
		classnames[1].append(line.lstrip(" ").rstrip("\n"))
castingmods = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
#halfcast t/f
#hitdice use dice from earlier

#
# ClassSpell
#

#random class ID
#random Spell ID

#
# Character
#

characternames = [[],[],[]]
with open("txtfiles/first-names.txt") as f:
	lines = f.readlines()
	for line in lines:
		characternames[0].append(line.rstrip("\n"))
with open("txtfiles/middle-names.txt") as f:
	lines = f.readlines()
	for line in lines:
		characternames[1].append(line.rstrip("\n"))
with open("txtfiles/names.txt") as f:
	lines = f.readlines()
	for line in lines:
		characternames[2].append(line.rstrip("\n"))
#select 4 different classIDs
#4 random numbers between 1 and 5


#
# Background
#

#ID
backgrounds = []
with open("txtfiles/gistfile1.txt") as f:
	lines = f.readlines()
	for line in lines:
		backgrounds.append(line.rstrip('\n'))

data = open("data.sql", "w+")
# infileUsage = open("/var/lib/mysql-files/infileUsage.txt", "w+")
# infileEffect = open("/var/lib/mysql-files/infileEffect.txt", "w+")
# infileSpell = open("/var/lib/mysql-files/infileSpell.txt", "w+")
# infileClass = open("/var/lib/mysql-files/infileClass.txt", "w+")
# infileClassSpell = open("/var/lib/mysql-files/infileClassSpell.txt", "w+")
# infileBackground = open("/var/lib/mysql-files/infileBackground.txt", "w+")
# infileCharacter = open("/var/lib/mysql-files/infileCharacter.txt", "w+")

# Usages
for ID in range(1,55001):
	usageID = ID
	name = r.choice(usagenames)
	data.write("INSERT INTO `cpsc408_2295968`.`Usage` VALUES ({},'{}');\n".format(usageID, name))
	# infileUsage.write("{},{}\n".format(usageID, name))

#effects
for ID in range(1,1005001):
	effectID = ID
	parentUsage = r.randint(1,55000)
	save = r.choice(saves)
	damage = str(r.randint(1,100)) + r.choice(dice)
	text = r.choice(texts)
	data.write("INSERT INTO `cpsc408_2295968`.`Effect` VALUES ({},{},'{}','{}','{}');\n".format(effectID, parentUsage, save, damage, text))
	# infileEffect.write("{},{},{},{},{}\n".format(effectID, parentUsage, save, damage, text))

#spells
for ID in range(1,55001):
	spellID = ID
	name = r.choice(spellnames[0]) + ' ' +  r.choice(spellnames[2]) + ' ' + r.choice(spellnames[1])
	level = r.randint(0,9)
	school = r.choice(schools)
	castingTime = r.choice(castingtimes)
	rang = r.randint(-1,5280)
	target = r.choice(targets)
	hasVerbal = r.randint(0,1)
	hasSomatic = r.randint(0,1)
	materialComponents = r.choice(materialcomponents)
	concentration = r.randint(0,1)
	duration = r.randint(-1,3600)
	primaryEffect = r.randint(1,1005000)
	secondaryEffect = r.randint(1,1005000)
	data.write("INSERT INTO `cpsc408_2295968`.`Spell` VALUES ({},'{}',{},'{}','{}',{},'{}',{},{},'{}',{},{},{},{});\n".format(spellID, name, level, school, castingTime, rang, target, hasVerbal, hasSomatic, materialComponents, concentration, duration, primaryEffect, secondaryEffect))
	# infileSpell.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(spellID, name, level, school, castingTime, rang, target, hasVerbal, hasSomatic, materialComponents, concentration, duration, primaryEffect, secondaryEffect))

# Class
for ID in range(1,5501):
	classID = ID
	name = r.choice(classnames[0]) + ' ' + r.choice(classnames[1]) + ' ' + r.choice(classnames[2])
	castingMod = r.choice(castingmods)
	halfCast = r.randint(0,1)
	hitDie = r.choice(dice)
	data.write("INSERT INTO `cpsc408_2295968`.`Class` VALUES ({},'{}','{}',{},'{}');\n".format(classID, name, castingMod, halfCast, hitDie))
	# infileClass.write("{},{},{},{},{}\n".format(classID, name, castingMod, halfCast, hitDie))

#ClassSpell
for ID in range(1,55001):
	classID = r.randint(1,5500)
	spellID = r.randint(1,55000)
	data.write("INSERT INTO `cpsc408_2295968`.`ClassSpell` VALUES ({},{});\n".format(classID, spellID))
	# infileClassSpell.write("{},{}\n".format(classID, spellID))

#Background
for ID in range(1,55001):
	backgroundID = ID
	name = r.choice(backgrounds)
	data.write("INSERT INTO `cpsc408_2295968`.`Background` VALUES ({},'{}');\n".format(backgroundID, name))
	# infileBackground.write("{},{}\n".format(backgroundID, name))

#Character
for ID in range(1,55001):
	characterID = ID
	name = r.choice(characternames[0]) + ' ' + r.choice(characternames[1]) + ' ' + r.choice(characternames[2])
	bg = r.randint(1,55000)
	cass = r.randint(1,5500)
	level = r.randint(1,5)
	clss2 = r.randint(1,5500)
	level2 = r.randint(0,5)
	clss3 = r.randint(1,5500)
	level3 = r.randint(0,5)
	clss4 = r.randint(1,5500)
	level4 = r.randint(0,5)
	data.write("INSERT IGNORE INTO `cpsc408_2295968`.`Character` VALUES ({},'{}',{},{},{},{},{},{},{},{},{});\n".format(characterID, name, cass, bg, level, clss2, level2, clss3, level3, clss4, level4))
	# infileCharacter.write("{},{},{},{},{},{},{},{},{},{},{}\n".format(characterID, name, bg, cass, level, clss2, level2, clss3, level3, clss4, level4))
	
data.close()
infileUsage.close()
infileEffect.close()
infileSpell.close()
infileClass.close()
infileClassSpell.close()
infileBackground.close()
infileCharacter