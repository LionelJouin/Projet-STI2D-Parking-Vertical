# http://www.science-emergence.com/Python/PythonFAQ/CreateDataBaseTablePythonSqlite3/
# http://python.developpez.com/cours/apprendre-python3/?page=page_18#L18-A-6
# http://apprendre-python.com/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite
# http://perso.telecom-paristech.fr/~gramfort/liesse_python/5-BDD.html


import sqlite3

from tkinter import *

#data\donnees

conn = sqlite3.connect('database.db')

cursor = conn.cursor()


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

'''
code = "1110f6f99"
accept = 0
entrantsortant = 2
place = 15
dateheure = "20/02/2015 - 15:19"
cursor.execute("INSERT INTO utilisation(utilisation_code, utilisation_accept, utilisation_entrantsortant, utilisation_place, utilisation_dateheure) VALUES(?,?,?,?,?)", (code, accept, entrantsortant, place, dateheure))
'''

id = 0
code = "0100b87a09"
dispo = 0
predef = 1
active = 1
cursor.execute("""UPDATE places SET places_code = ?, places_dispo = ?, places_predef = ?, places_active = ? WHERE places_id = ?""", (code, dispo, predef, active, id, ))

conn.commit()


cursor.execute("SELECT * FROM places")
places = list(cursor)
print("places :")
print()
print(places)
print()
print(places[0][0])
print(places[0][1])
print(places[0][2])
print(places[0][3])
print(places[0][4])
print()
print()
cursor.execute("SELECT * FROM utilisation")
#utilisation = list(cursor)
utilisation = cursor.fetchall() 
print("utilisation :")
print()
print(utilisation)


while 1:
	pass