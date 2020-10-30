# Python interface to Spell Database

import sqlite3
from sqlite3 import Error
import sys
import re ### SOMEHOW SANITIZE INPUT

if len(sys.argv) != 2:
	print('Usage: python3 Interface.py <database file name>')

# Opening connection to database
conn = None
try:
	conn = sqlite3.connect(sys.argv[1])
except Error as e:
	print(e)

if conn == None:
	sys.exit("Failed to connect to database. Exiting Program.")

c = conn.cursor()

c.execute('SELECT name FROM sqlite_master')
if c.fetchone() == None: #may cause an issue (switch to '')
	with open('Black_schema.sql') as schema:
		c.executescript(schema.read())



# Adds record to Class table
def insert_Class(class_name=None):
	
	cid = generate_ID('Class')

	if not class_name:
		class_name = input('Class name: ')
	tup = (cid, class_name)
	c.execute('INSERT INTO Class VALUES (?,?)', tup)


# Deletes record from Class table
def delete_Class(cid=None):

	if not cid:
		cid = int(input('ID of Class to delete: '))
	tup = (cid,)
	c.execute('DELETE FROM Class WHERE cid=?', tup)


# Adds record to Spell table
def insert_Spell(spell_name=None, level=None, school=None, casting_time=None, spell_range=None, target=None, has_verbal=None, has_somatic=None, material_components=None, concentration=None, duration=None, primary_usage=None, secondary_usage=None):

	sid = generate_ID('Spell')

	if not spell_name:
		spell_name = input('Spell name: ')
	if not level:
		level = int(input('Spell level (0-9): '))
	if not school:
		school = input('Spell school: ')
	if not casting_time:
		casting_time = input('Casting time: ')
	if not spell_range:
		spell_range = int(input('Spell range (integer): '))
	if not target:
		target = input('Spell target: ')
	if has_verbal == None:
		has_verbal = int(input('Spell has Verbal component (0 = no, 1 = yes): '))
	if has_somatic == None:
		has_somatic = int(input('Spell has Somatic component (0 = no, 1 = yes: '))
	if not material_components:
		material_components = input('Material components (\'n\' if no material components): ')
		if material_components == 'n':
			material_components = None
	elif material_components == 'n':
		material_components = None
	if concentration == None:
		concentration = int(input('Spell is Concentration (0 = no, 1 = yes): '))
	if not duration:
		duration = input('Spell duration: ')
	if not primary_usage:
		primary_usage = int(input('Primary spell usage (Usage ID, or 0 for none): '))
		if primary_usage == 0:
			primary_usage = None
	if not secondary_usage:
		secondary_usage = int(input('Secondary spell usage (Usage ID, or 0 for none): '))
		if secondary_usage == 0:
			secondary_usage = None

	tup = (sid, spell_name, level, school, casting_time, spell_range, target, has_verbal, has_somatic, material_components, concentration, duration, primary_usage, secondary_usage)
	c.execute('INSERT INTO Spell VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', tup)


# Deletes record from Spell table
def delete_Spell(sid=None):

	if not sid:
		sid = int(input('ID of Spell to delete: '))
	tup = (sid,)
	c.execute('DELETE FROM Spell WHERE sid=?', tup)


# Adds record bla bla bla
def insert_Class_Spell(cid=None, sid=None):

	if not cid:
		cid = int(input('ID of Class to tie to Spell: '))
	if not sid:
		sid = int(input('ID of Spell to tie to Class: '))

	tup = (cid,sid)
	c.execute('INSERT INTO Class_Spell VALUES (?,?)', tup)


# Deletes record yada yada
def delete_Class_Spell(cid=None, sid=None):

	if not cid:
		cid = int(input('ID of Class to remove tie from: '))
	if not sid:
		sid = int(input('ID of Spell to remove tie from: '))

	tup = (cid,sid)
	c.execute('DELETE FROM Class_Spell WHERE cid=?,sid=?', tup)


# Take a guess
def insert_Usage(usage_name=None):

	uid = generate_ID('Usage')

	if not usage_name:
		usage_name = input('Usage name: ')
	tup = (uid, usage_name)
	c.execute('INSERT INTO Usage VALUES (?,?)', tup)


# Nothing new here
def delete_Usage(uid=None):

	if not uid:
		uid = int(input('ID of Usage to delete: '))
	tup = (uid,)
	c.execute('DELETE FROM Usage WHERE uid=?', tup)


# Offers user 9 different query options, some of which require further input
def query():

	print('Which query to execute?')
	print('\t1) List all spells from a certain school')
	print('\t2) List all spell names for a certain class')
	print('\t3) List all spell names, levels, and schools, grouped by class')
	print('\t4) List all spell names, grouped by primary usage')
	print('\t5) List all spell names of a certain level or lower')
	print('\t6) Get all Spell info by name')
	print('\t7) Get all Spell info by ID')
	print('\t8) List all Class IDs and Names')
	print('\t9) List all Usage IDs and Names')

	opt = int(input(' > '))

	# Spells by School
	if opt == 1:
		print('Which school of magic?')
		for row in c.execute('SELECT DISTINCT school FROM Spell ORDER BY school ASC'):
			print(' - ' + row[0])
		school = input(' > ')
		tup = (school,)
		c.execute('SELECT sid, name, level, school FROM Spell WHERE school=?', tup)
		print(c.fetchall())

	# Spells by a chosen class
	elif opt == 2:
		print('Which class?')
		for row in c.execute('SELECT DISTINCT name FROM Class ORDER BY name ASC'):
			print(' - ' + row[0])
		cl = input(' > ')
		tup = (cl,)
		c.execute('SELECT Spell.sid, Spell.name, level, school FROM Class NATURAL JOIN Class_Spell INNER JOIN Spell ON Class_Spell.sid=Spell.sid WHERE Class.name=?', tup)
		print(c.fetchall())

	# Spells grouped by class
	elif opt == 3:
		# Make Spell name, level, and school into a group aggregate
		c.execute("SELECT Class.name, group_concat(Spell.name || ', ' || level || ', ' || school, '; ') FROM Class NATURAL JOIN Class_Spell INNER JOIN Spell ON Class_Spell.sid=Spell.sid GROUP BY Class.name ORDER BY Class.name ASC")
		print(c.fetchall())

	# Spells by usage
	elif opt == 4:
		c.execute('SELECT Usage.name, group_concat(Spell.name) FROM Usage INNER JOIN Spell ON Spell.primary_usage=Usage.uid GROUP BY Usage.name')
		print(c.fetchall())

	# Spells of given level or lower
	elif opt == 5:
		lvl = int(input('Max level of spell to display (0-9): '))
		tup = (lvl,)
		c.execute('SELECT sid, name, level, school FROM Spell WHERE level<=? ORDER BY level ASC', tup)
		print(c.fetchall())

	# Specific Spell by name
	elif opt == 6:
		nm = input('Spell name to look up: ')
		tup = (nm,)
		c.execute('SELECT * FROM Spell WHERE name=?', tup)
		print(c.fetchall())

	# Specific Spell by ID
	elif opt == 7:
		ID = int(input('Spell ID to look up: '))
		tup = (ID,)
		c.execute('SELECT * FROM Spell WHERE sid=?', tup)
		print(c.fetchall())

	# List all classes
	elif opt == 8:
		c.execute('SELECT * FROM Class ORDER BY name ASC')
		print(c.fetchall())

	# List all usages
	elif opt == 9:
		c.execute('SELECT * FROM Usage ORDER BY name ASC')
		print(c.fetchall())

	else:
		print('Invalid input.')
		return


def generate_ID(table):

	c.execute('SELECT COUNT(*) FROM '+table+';')
	
	table_root = None
	idpref = None
	if table == 'Spell':
		table_root = 10000
		idpref = 's'
	elif table == 'Class':
		table_root = 20000
		idpref = 'c'
	elif table == 'Usage':
		table_root = 30000
		idpref = 'u'


	r = c.fetchone()
	if int(r[0]) == 0:
		id = table_root
	else:
		# Find the minimum open ID above table_root
		id = table_root
		for row in c.execute('SELECT ' + idpref + 'id FROM ' + table + ' ORDER BY ' + idpref + 'id ASC'):
			if row[0] == id:
				id += 1
			else:
				break

	print(id)

	return id


def commit():
	conn.commit()
	print('Changes commited to Database')


def exit():
	commit()
	conn.close()
	sys.exit(0)


print(' ----- Lloyd\'s 5e Spell Database -----')

# MAIN INTERFACE LOOP: Presents user with 10 options, some of which redirect to other option selections
# Continues until the program crashes or the user quits
while True:
	
	print('\nSelect an option:')
	print('\t1) Insert Record')
	print('\t2) Delete Record')
	print('\t3) Insert Records from txt file')
	print('\t4) Delete Records from txt file')
	print('\t5) Query Table')
	print('\t6) Commit Changes to file')
	print('\t7) Database info blurb')
	print('\t8) Print text file formatting guide')
	print('\t9) Exit')
	print('\t10) Exit without saving')

	opt = int(input(' > '))

	# Insert records manually by answering prompts
	if opt == 1:
		print('Which table?')
		print('\t1) Class')
		print('\t2) Spell')
		print('\t3) Add Spell to Class\'s Spell list')
		print('\t4) Usage')

		opt = int(input(' > '))

		if opt == 1:
			insert_Class()
		elif opt == 2:
			insert_Spell()
		elif opt == 3:
			insert_Class_Spell()
		elif opt == 4:
			insert_Usage()
		else:
			print('Invalid input.')
			continue

	# Delete records manually by entering an ID
	elif opt == 2:
		print('Which table?')
		print('\t1) Class')
		print('\t2) Spell')
		print('\t3) Add Spell to Class\'s Spell list')
		print('\t4) Usage')

		opt = int(input(' > '))

		if opt == 1:
			delete_Class()
		elif opt == 2:
			delete_Spell()
		elif opt == 3:
			delete_Class_Spell()
		elif opt == 4:
			delete_Usage()
		else:
			print('Invalid input.')
			continue

	# Insert many records at once from formatted text file
	elif opt == 3:
		txt = input('Name of Text File: ')
		
		print('Which table?')
		print('\t1) Class')
		print('\t2) Spell')
		print('\t3) Add Spell to Class\'s Spell list')
		print('\t4) Usage')

		opt = int(input(' > '))

		with open(txt) as f:
			if opt == 1:
				for line in f.readlines():
					args = line.split('\n|')
					insert_Class(class_name=args[0])
			elif opt == 2:
				linenum = 0
				for line in f.readlines():
					linenum += 1
					args = line.split('\n|')
					if len(args) != 13:
						print('Bad format at line ' + str(linenum))
						continue
					insert_Spell(spell_name=args[0], level=int(args[1]), school=args[2], casting_time=args[3], spell_range=int(args[4]), target=args[5], has_verbal=int(args[6]), has_somatic=int(args[7]), material_components=args[8], concentration=int(args[9]), duration=args[10], primary_usage=int(args[11]), secondary_usage=int(args[12]))
			elif opt == 3:
				linenum = 0
				for line in f.readlines():
					linenum += 1
					args = line.split('\n|')
					if len(args) != 2:
						print('Bad format at line ' + str(linenum))
						continue
					insert_Class_Spell(cid=int(args[0]), sid=int(args[1]))
			elif opt == 4:
				for line in f.readlines():
					args = line.split('\n|')
					insert_Usage(usage_name=args[0])
			else:
				print('Invalid input.')
				continue

	# Delete records from list of IDs in a file
	elif opt == 4:
		txt = input('Name of Text File: ')

		print('Which table?')
		print('\t1) Class')
		print('\t2) Spell')
		print('\t3) Add Spell to Class\'s Spell list')
		print('\t4) Usage')

		opt = int(input(' > '))

		with open(txt) as f:
			if opt == 1:
				for line in f.readlines():
					delete_Class(cid=int(line))
			elif opt == 2:
				for line in f.readlines():
					delete_Spell(sid=int(line))
			elif opt == 3:
				linenum = 0
				for line in f.readlines():
					linenum += 1
					args = line.split('|')
					if len(args) != 2:
						print('Bad format at line ' + str(linenum))
					delete_Class_Spell(cid=int(args[0]), sid=int(args[1]))
			elif opt == 4:
				for line in f.readlines():
					delete_Usage(uid=int(line))
			else:
				print('Invalid input.')
				continue

	# Directs user to a menu to query the table
	elif opt == 5:
		query()

	# Saves all changes to file without quitting
	elif opt == 6:
		commit()

	# Prints basic info about database layout
	elif opt == 7:
		print('The database has 4 tables: Class, Spell, Class_Spell, and Usage. All attribute type not specified are strings.')
		print('Class attributes are ID(int) and name, representing D&D 5e Player classes.')
		print('Spell attributes are ID(int), name, level(int), school, casting time, range(int), target, has verbal component(int), has somatic component(int), material components, is concentration(int), duration, primary usage ID(int), and secondary usage ID(int), representing spells in D&D 5e.')
		print('Class_Spell attributes are Class ID(int) and Spell ID(int). Having a class ID and spell ID in the same row on this table means that the spell is a member of the class\'s spell list')
		print('Usage attributes are Usage ID(int) and name, representing the broad reason one might use a spell (EG Buff, Debuff, Damage, Healing, etc)')

	# Prints formatting guide for text files to use with options 3 and 4
	elif opt == 8:
		print('All text files with multiple attributes (insert spell and insert and delete Class-Spell) should have | dilineated attributes, and for all files, a new line represents a new row in the table.')
		print('For insertion of Class and Usage, simply provide a list of Class or Usage names.')
		print('Order for Insertion of Spells: <name>|<level>|<school>|<casting time>|<range>|<target>|<has verbal>|<has somatic>|<material components>|<is concentration>|<duration>|<primary usage>|<secondary usage>')
		print('For deletion of Class, Spell, and Usage, provide a list of Class, Spell, or Usage IDs.')
		print('Order for Class-Spell (insert and delete): <class ID>|<spell ID>')

	# Quits and saves
	elif opt == 9:
		commit()
		sys.exit('Successful termination')

	# Quits without saving
	elif opt == 10:
		sys.exit('Successful termination')