# Python interface to Spell Database

import sqlite3
from sqlite3 import Error
import sys
import re ### SOMEHOW SANITIZE INPUT

if len(sys.argv) != 2:
	print('Usage: python3 Interface.py <database file name>')

conn = None
try:
	conn = sqlite3.connect(sys.argv[1])
except Error as e:
	print(e)

if conn = None:
	sys.exit("Failed to connect to database. Exiting Program.")

c = conn.Cursor()

c.execute('SELECT name FROM sqlite_master')
if c.fetchone() == None: #may cause an issue (switch to '')
	with open('Black_schema.sql') as schema:
		c.executescript(schema.read())


def insert_Class(class_name=None):
	
	cid = generate_ID('Class')

	if not class_name:
		class_name = input('Class name: ')
	tup = (cid, class_name)
	c.execute('INSERT INTO Class VALUES (?,?)', tup)


def delete_Class(cid=None):

	if not cid:
		cid = int(input('ID of Class to delete: '))
	tup = (cid,)
	c.execute('DELETE FROM Class WHERE cid=?', tup)


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
	if concentration == None:
		concentration = int(input('Spell is Concentration (0 = no, 1 = yes): '))
	if not duration:
		duration = input('Spell duration: ')
	if not primary_usage:
		primary_usage = int(input('Primary spell usage (Usage ID, or \'n\' for none): '))
		if primary_usage[0].lower():
			primary_usage = None
	if not secondary_usage:
		secondary_usage = int(input('Secondary spell usage (Usage ID, or \'n\' for none): '))
		if secondary_usage[0].lower():
			secondary_usage = None

	tup = (sid, spell_name, level, school, casting_time, spell_range, target, has_verbal, has_somatic, material_components, concentration, duration, primary_usage, secondary_usage)
	c.execute('INSERT INTO Spell VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', tup)



def delete_Spell(sid=None):

	if not sid:
		sid = int(input('ID of Spell to delete: '))
	tup = (sid,)
	c.execute('DELETE FROM Spell WHERE sid=?', tup)


def insert_Class_Spell(cid=None, sid=None):

	if not cid:
		cid = int(input('ID of Class to tie to Spell: '))
	if not sid:
		sid = int(input('ID of Spell to tie to Class: '))

	tup = (cid,sid)
	c.execute('INSERT INTO Class_Spell VALUES (?,?)', tup)



def delete_Class_Spell(cid=None, sid=None):

	if not cid:
		cid = int(input('ID of Class to remove tie from: '))
	if not sid:
		sid = int(input('ID of Spell to remove tie from: '))

	tup = (cid,sid)
	c.execute('DELETE FROM Class_Spell WHERE cid=?,sid=?', tup)


def insert_Usage(usage_name=None):

	uid = generate_ID('Usage')

	if not usage_name:
		usage_name = input('Usage name: ')
	tup = (uid, usage_name)
	c.execute('INSERT INTO Usage VALUES (?,?)', tup)


def delete_Usage(uid=None):

	if not uid:
		uid = int(input('ID of Usage to delete: '))
	tup = (uid,)
	c.execute('DELETE FROM Usage WHERE uid=?', tup)


def query():
# Get class spell lists: Group and order by Class then group by ascending spell level and then order by ascending spell name
	
	print('Which query to execute?')
	print('\t1) List all spells from a certain school')
	print('\t2) List all spell names for a certain class')
	print('\t3) List all spell names, levels, and schools, grouped by class')
	print('\t4) List all spell names, grouped by primary usage')
	print('\t5) List all spell names of a certain level or lower')
	print('\t6) Get all Spell info by name')
	print('\t7) Get all Spell info by ID')

	opt = int(input(' > '))

	if opt == 1:
		print('Which school of magic?')
		for row in c.execute('SELECT DISTINCT school FROM Spell ORDER BY school ASC'):
			print(' - ' + row[0])
		school = input(' > ')
		tup = (school,)
		c.execute('SELECT sid, name, level, school FROM Spell WHERE school=?', tup)
		print(c.fetchall())

	if opt == 2:
		print('Which class?')
		for row in c.execute('SELECT DISTINCT name FROM Class ORDER BY name ASC'):
			print(' - ' + row[0])
		cl = input(' > ')
		tup = (cl,)
		c.execute('SELECT sid, Spell.name, level, school FROM Class NATURAL JOIN Class_Spell NATURAL JOIN Spell WHERE Class.name=?', tup)
		print(c.fetchall())

	if opt == 3:
		c.execute('SELECT Class.name, Spell.name, level, school FROM Class NATURAL JOIN Class_Spell NATURAL JOIN Spell GROUP BY Class.name ORDER BY Class.name ASC')
		print(c.fetchall())

	if opt == 4:
		c.execute('SELECT Usage.name, Spell.name FROM Usage NATURAL JOIN Spell GROUP BY Usage.name')
		print(c.fetchall())

	if opt == 5:
		lvl = int(input('Max level of spell to display (0-9): '))
		tup = (lvl,)
		c.execute('SELECT sid, name, level, school FROM Spell WHERE level<=? ORDER BY level ASC')
		print(c.fetchall())

	if opt == 6:
		nm = input('Spell name to look up: ')
		tup = (nm,)
		c.execute('SELECT * FROM Spell WHERE name=?', tup)
		print(c.fetchall())

	if opt == 7:
		ID = int(input('Spell ID to look up: '))
		tup = (ID,)
		c.execute('SELECT * FROM Spell WHERE sid=?', tup)
		print(c.fetchall())


def generate_ID(table):

	c.execute('SELECT COUNT(*) FROM '+table+';')
	
	table_root = None
	idpref = None
	if table == 'Class':
		table_root = 20000
		idpref = 'c'
	else if table == 'Usage':
		table_root = 30000
		idpref = 'u'
	else if table == 'Spell':
		table_root == 10000
		idpref = 's'


	tup = (idpref, table, idpref)
	if int(c.fetchone()) == 0:
		id = table_root
	else:
		# Find the minimum open ID above table_root
		id = table_root
		for row in c.execute('SELECT ?id FROM ? ORDER BY ?id ASC', tup):
			if row[0] == id:
				id += 1
			else:
				break

	return id


def commit():
	conn.commit()


def exit():
	commit()
	conn.close()
	sys.exit(0)

while true:
	# Loop for interface

