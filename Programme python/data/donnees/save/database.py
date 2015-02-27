import os
import sqlite3

from src.style.funct import *

listplaces = [(0, '', 1, 0, 1), (1, '', 1, 0, 1), (2, '', 1, 0, 1), (3, '', 1, 0, 1), (4, '', 1, 0, 1), (5, '', 1, 0, 1), (6, '', 1, 0, 1), (7, '', 1, 0, 1), (8, '', 1, 0, 1), (9, '', 1, 0, 1), (10, '', 1, 0, 1), (11, '', 1, 0, 1), (12, '', 1, 0, 1), (13, '', 1, 0, 1), (14, '', 1, 0, 1)]
listutilisation = [(1, '0000000000', 0, 2, 15), (2, '0000000000', 0, 2, 15), (3, '0000000000', 0, 2, 15), (4, '0000000000', 0, 2, 15), (5, '0000000000', 0, 2, 15), (6, '0000000000', 0, 2, 15), (7, '0000000000', 0, 2, 15), (8, '0000000000', 0, 2, 15), (9, '0000000000', 0, 2, 15), (10, '0000000000', 0, 2, 15)]
connexion = None
cursor = None

def load_database():
	
	global connexion
	global cursor

	connexion = sqlite3.connect('data/donnees/database.db')
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
	  utilisation_code INTEGER,
	  utilisation_accept INTEGER,
	  utilisation_entrantsortant INTEGER,
	  utilisation_place INTEGER,
	  utilisation_dateheure TEXT
	)
	""")

	connexion.commit()

	load_places()
	load_utilisation()

def get_connexion():
	return(connexion)

def get_cursor():
	return(cursor)

def load_places():
	cursor.execute("SELECT * FROM places")
	global listplaces
	listplaces = cursor.fetchall() 
	a = 0
	while a<15:
		set_place_active(listplaces[a][0], listplaces[a][4])
		set_place_predef(listplaces[a][0], listplaces[a][3], listplaces[a][1])
		set_place_dispo(listplaces[a][0], listplaces[a][2], listplaces[a][1])
		print(listplaces[a])
		a += 1

def load_utilisation():
	cursor.execute("SELECT * FROM utilisation ORDER BY utilisation_id DESC LIMIT 10")
	global listutilisation
	listutilisation = cursor.fetchall() 
	a = 9
	while a>-1:
		add_last_places(listutilisation[a][4], listutilisation[a][1], listutilisation[a][3], listutilisation[a][2], listutilisation[a][5])
		a -= 1

def update_place(self, place, code, dispo, predef, active):
	cursor.execute("""UPDATE places SET places_code = ?, places_dispo = ?, places_predef = ?, places_active = ? WHERE places_id = ?""", (code, dispo, predef, active, place, ))
	connexion.commit()
