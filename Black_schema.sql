# Schema for a 5e D&D Spell Database

Class(cid, name)
Spell(sid, name, level, school, casting_time, range, target, has_verbal, has_somatic, material_components, concentration, duration, primary_usage, secondary_usage) #duration=string, 
Class_Spell(cid, sid)
Usage(uid, name)

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
	has_verbal integer,
	has_somatic integer, 
	material_components varchar(200), # Empty if none
	concentration integer,
	duration integer, # 0=Instantaneous, -1=until dispelled, otherwise by round (10=minute)
	primary_usage integer foreign key references Usage(uid),
	secondary_usage integer foreign key references Usage(uid)
);

create table Class_Spell (
	cid integer foreign key references Class(cid),
	sid integer foreign key references Spell(sid),
	primary key (cid, sid)
);

create table Usage ( # Mooch off of Dndbeyond spell tags
	uid integer primary key,
	name varchar(20)
);
