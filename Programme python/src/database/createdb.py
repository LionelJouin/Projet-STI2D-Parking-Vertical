import os
import time
import sqlite3

connexion = sqlite3.connect('database.db', check_same_thread = False, isolation_level = None) # arguments utile pour passer a travers les threads
cursor = connexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS places (
	places_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	places_code TEXT,
	places_dispo INTEGER,
	places_predef INTEGER,
	places_active INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisation (
	utilisation_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	utilisation_code TEXT,
	utilisation_accept INTEGER,
	utilisation_entrantsortant INTEGER,
	utilisation_place INTEGER,
	utilisation_dateheure TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS badges (
	badges_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	badges_code TEXT,
	badges_dateheure TEXT,
	badges_place INTEGER,
	badges_active INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS parameters (
	parameters_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	parameters_name TEXT,
	parameters_value TEXT
)
""")

connexion.commit()


cursor.execute("SELECT Count(*) FROM places")
size_place = cursor.fetchall() 
size_places = size_place[0][0]


if size_places!=15:
	a = 0
	while a<15:
		cursor.execute("INSERT INTO places(places_id, places_code, places_dispo, places_predef, places_active) VALUES(?,?,?,?,?)", (a, "", 1, 0, 1))
		connexion.commit()
		a += 1




cursor.execute("SELECT Count(*) FROM parameters")
size_parameter = cursor.fetchall() 
size_parameters = size_parameter[0][0]

nb_parameters = 3

parameters_name = ["ip", "port", "etat_parking"]
parameters_value = ["192.168.1.200", "1337", "0"]

# 0 ip
# 1 port
# 2 etat_parking
# 3
# 4

if size_parameters!=nb_parameters:
	a = 0
	while a<nb_parameters:
		cursor.execute("INSERT INTO parameters(parameters_id, parameters_name, parameters_value) VALUES(?,?,?)", (a, parameters_name[a], parameters_value[a]))
		connexion.commit()
		a += 1
