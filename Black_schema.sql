# Schema for a 5e D&D Spell Database

Class(cid, name)
Spell(sid, name, level, school, casting_time, range, target, components, material_components, concentration, duration) # Components=1-7 that works like rwx, duration=string, 
Spell_List(cid, sid)
Spell_Effects(sid, summary, has_attack, attack_type, has_save, save_type, deals_damage, avg_damage, full_damage, imposes_condition, condition)

create table Class (
	cid integer primary key,
	name varchar(10),
);

create table Spell (
	sid integer primary key,
	name varchar(40),
	level integer,
	school varchar(15),
	casting_time varchar(15),
	range integer, # 0=self, 1=touch, -1=unlimited
	target varchar(25),
	components integer, # xyz binary, x=vocal, y=somatic, z=material
	material_components varchar(200),
	concentration boolean,
	duration integer, # 0=Instantaneous, -1=until dispelled, otherwise by round (10=minute)
);

create table Spell_List (
	cid integer foreign key references Class(cid),
	sid integer foreign key references Spell(sid),
	primary key (cid, sid)
);

create table Spell_Effects (
	sid integer primary key foreign key references Spell(sid),
	summary varchar(1000),
	has_attack boolean,
	attack_type varchar(10),
	has_save boolean,
	save_type varchar(5),
	deals_damage boolean,
	avg_damage integer,
	full_damage varchar(30),
	imposes_condition boolean,
	condition varchar(50)
);

