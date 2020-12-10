-- Schema for a 5e D&D Spell Database
/*
Class(cid, name)
Spell(sid, name, level, school, casting_time, range, target, has_verbal, has_somatic, material_components, concentration, duration, primary_usage, secondary_usage) -- duration=string, 
Class_Spell(cid, sid)
Usage(uid, name)
*/

PRAGMA foreign_keys = ON;

create table Class (
	cid integer not null primary key,
	name varchar(10)
);

create table Spell (
	sid integer not null primary key,
	name varchar(40),
	level integer,
	school varchar(15),
	casting_time varchar(15),
	range integer, -- 0=self, 1=touch, -1=unlimited
	target varchar(25),
	has_verbal integer,
	has_somatic integer, 
	material_components varchar(200), -- Empty if none
	concentration integer,
	duration integer, -- 0=Instantaneous, -1=until dispelled, otherwise by round (10=minute)
	primary_usage integer,
	secondary_usage integer,
	foreign key(primary_usage) references Usage(uid),
	foreign key(secondary_usage) references Usage(uid)
);

create table Class_Spell (
	cid integer not null,
	sid integer not null,
	foreign key(cid) references Class(cid),
	foreign key(sid) references Spell(sid),
	primary key (cid, sid)
);

create table Usage ( -- Mooch off of Dndbeyond spell tags
	uid integer not null primary key,
	name varchar(20)
);
