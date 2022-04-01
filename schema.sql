DROP TABLE IF EXISTS flavors;

CREATE TABLE flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hourlyprice REAL NOT NULL,
    monthlyprice REAL NOT NULL
);

DROP TABLE IF EXISTS storage;

CREATE TABLE storage (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	hourlyprice REAL NOT NULL,
	monthlyprice REAL NOT NULL
);

DROP TABLE IF EXISTS network;

CREATE TABLE network (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	hourlyprice REAL NOT NULL,
	monthlyprice REAL NOT NULL
);

DROP TABLE IF EXISTS licenses;

CREATE TABLE licenses (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	hourlyprice NOT NULL,
	monthlyprice NOT NULL
);


