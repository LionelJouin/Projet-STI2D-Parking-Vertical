import os
import time
import socket
import sqlite3

from tkinter import *
from math import *

screen_w = screen_h = width_pxl = height_pxl = pos_x = pos_y = 0
width_percent = height_percent = 80
selected_menu = 0
selected_submenu = 0
connectedtosystem = 0
connectedtointernet = 0
checking_var = {}
sock = ""
checking_var['chargement'] = 0

#convertir pixel en pourcent
def pxltopercent(pixel, on):
	return(int(pixel*on/100))

def define_sizescreen(size):
	global screen_w
	global screen_h
	screen_w, screen_h = size

#definie les variables de position
def define_sizenpos(size, pos):
	global pos_x
	global pos_y
	global width_pxl
	global height_pxl
	pos_x, pos_y = pos
	width_pxl, height_pxl = size

#recupere les variables
def infos(parametre):
	if parametre == "largeur_ecran": 
		global screen_w
		return ( screen_w )
	elif parametre == "hauteur_ecran":
		global screen_h
		return ( screen_h )
	elif parametre == "largeur_fenetre":
		global width_pxl
		return ( width_pxl )
	elif parametre == "hauteur_fenetre":
		global height_pxl
		return ( height_pxl )
	elif parametre == "largeur_fenetre_percent":
		global width_percent
		return ( width_percent )
	elif parametre == "hauteur_fenetre_percent":
		global height_percent
		return ( height_percent )
	elif parametre == "position_x":
		global pos_x
		return ( pos_x )
	elif parametre == "position_y":
		global pos_y
		return ( pos_y )

'''
------------------------------------------------------
menu
'''
def define_selected_menu(id):
	global selected_menu
	selected_menu = id

def get_selected_menu():
	return(selected_menu)

def define_selected_submenu(id):
	global selected_submenu
	selected_submenu = id

def get_selected_submenu():
	return(selected_submenu)

'''
------------------------------------------------------
network
'''
def if_connectedtosystem(etat):
	global connectedtosystem
	connectedtosystem = etat

def is_connectedtosystem():
	return(connectedtosystem)

def if_connectedtointernet(etat):
	global connectedtointernet
	connectedtointernet = etat

def is_connectedtointernet():
	return(connectedtointernet)

def define_socket(socketvar):
	global sock
	sock = socketvar

def getting_socket():
	return(sock)

def envoyer(msg):
	if is_connectedtosystem()==1:
		time.sleep(0.05)
		sock.send(msg.encode('ascii'))

def load_config():
	a = 0
	while a<get_autorized_badges('size', 0):
		envoyer( 'Z'+get_autorized_badges('code', a) )
		a += 1

	a = 0
	while a<15:
		if place_dispo[a]==0:
			envoyer('V'+str(place_codes[a])+str(a))
		if place_predef[a]==1:
			envoyer( 'W'+str(place_codes[a])+str(a) )
		if place_active[a]==0:
			envoyer( 'y'+str(a) )
		a += 1

'''
------------------------------------------------------
gestion
'''

place_active = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1]
place_dispo = [0,1,0,0,1,1,1,1,1,1,1,1,1,1,1]
place_predef = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
place_codes = ['0100b87a09','','0001f2f00','1111c3a56','','','','','','','','','','','']

last_codes = ['0010e5b22', '0000c2f7ee', '1110f6f99', '0000f5b69', '0000c2f7ee', '1111c3a56', '0001f2f00', '0100b87a09', '0101a2c26', '0100b87a09']
last_accept = [0, 1, 0, 0, 1, 1, 1, 1, 0, 1] # 0 : non acceptees | 1 : acceptees
last_entrantsortant = [2, 1, 2, 2, 0, 0, 0, 1, 2, 0] # 0 : entrant | 1 : sortant
last_place = [15, 1, 15, 15, 1, 3, 2, 0, 15, 0]
last_dateheure = ['09/02/2015 - 20:24', '09/02/2015 - 20:20', '09/02/2015 - 19:13', '09/02/2015 - 15:04', '09/02/2015 - 08:24', '08/02/2015 - 23:55', '08/02/2015 - 22:25', '08/02/2015 - 18:14', '08/02/2015 - 17:26', '08/02/2015 - 16:59']
last_seconde = '20:24:15'

logsize = 0
logutilisations = [(1, '0000000000', 0, 2, 15), (2, '0000000000', 0, 2, 15), (3, '0000000000', 0, 2, 15), (4, '0000000000', 0, 2, 15), (5, '0000000000', 0, 2, 15), (6, '0000000000', 0, 2, 15), (7, '0000000000', 0, 2, 15), (8, '0000000000', 0, 2, 15), (9, '0000000000', 0, 2, 15), (10, '0000000000', 0, 2, 15), (11, '0000000000', 0, 2, 15), (12, '0000000000', 0, 2, 15), (13, '0000000000', 0, 2, 15), (14, '0000000000', 0, 2, 15), (15, '0000000000', 0, 2, 15), (16, '0000000000', 0, 2, 15), (17, '0000000000', 0, 2, 15)]

def is_place_active(id):
	return(place_active[id])

def set_place_active(id, etat, db=None):
	global place_active
	place_active[id] = etat
	if is_connectedtosystem()==1:
		if etat==1:
			envoyer('Y'+str(id))
		else:
			envoyer('y'+str(id))
	if checking_var['chargement']==1 and db==None:
		update_place(id, place_codes[id], place_dispo[id], place_predef[id], place_active[id])

def places_active():
	return(place_active)

def is_place_dispo(id):
	return(place_dispo[id])

def set_place_dispo(id, etat, code, db=None):
	global place_dispo
	place_dispo[id] = etat
	if etat==0:
		set_place_active(id, 1, 1)
		place_codes[id] = code
	else:
		if place_predef[id]==1:
			place_codes[id] = code
		else:
			place_codes[id] = ""
	if checking_var['chargement']==1 and db==None:
		update_place(id, place_codes[id], place_dispo[id], place_predef[id], place_active[id])

def places_dispo():
	return(place_dispo)

def is_place_predef(id):
	return(place_predef[id])

def set_place_predef(id, etat, code, db=None):
	global place_predef
	if etat==1:
		set_place_active(id, 1, 1)
	place_predef[id] = etat
	if checking_var['chargement']==1 and db==None:
		if etat==0:
			if is_place_dispo(id)==0:
				update_place(id, place_codes[id], place_dispo[id], place_predef[id], place_active[id])
			else:
				place_codes[id] = ""
				update_place(id, "", place_dispo[id], 0, place_active[id])
		else:
			place_codes[id] = code
			update_place(id, place_codes[id], place_dispo[id], place_predef[id], place_active[id])

def places_predef():
	return(place_predef)

def place_code(id):
	return(place_codes[id])

def set_place_code(id, etat):
	global place_codes
	place_codes[id] = etat

def all_places_code():
	return(place_codes)

def last_places(par, id):
	if par=='place':
		return(last_place[id])
	elif par=='code':
		return(last_codes[id])
	elif par=='dateheure':
		return(last_dateheure[id])
	elif par=='entrantsortant':
		return(last_entrantsortant[id])
	elif par=='etat':
		return(last_accept[id])
	elif par=='seconde':
		return(last_seconde)

def add_last_places(place, code, entrantsortant, etat, dateheure=None, db=None):
	global last_codes
	global last_accept
	global last_place
	global last_dateheure
	global last_seconde
	a = 9
	while a>0:
		last_codes[a] = last_codes[a-1]
		last_accept[a] = last_accept[a-1]
		last_entrantsortant[a] = last_entrantsortant[a-1]
		last_place[a] = last_place[a-1]
		last_dateheure[a] = last_dateheure[a-1]
		a -= 1
	last_codes[0] = code
	last_accept[0] = etat
	last_entrantsortant[0] = entrantsortant 
	last_place[0] = place
	if dateheure == None:
		last_dateheure[0] = time.strftime('%d/%m/%Y - %H:%M')
	else: 
		last_dateheure[0] = dateheure
	last_seconde = time.strftime('%H:%M:%S')
	if checking_var['chargement']==1 and  db==None:
		insert_utilisation(code, etat, entrantsortant, place, last_dateheure[0])

def get_autorized_badges(par, id):
	if par=='code':
		return(listcode[id][1])
	elif par=='dateheure':
		return(listcode[id][2])
	elif par=='place':
		return(listcode[id][3])
	elif par=='size':
		return(len(listcode))
	elif par=='seconde':
		return(last_seconde)
	elif par=='nbpage':
		return(ceil(len(listcode)/15))

def add_autorized_badges(code, dateheure, place):
	global last_seconde
	c = 0
	d = 0

	if place!="": # si on lie un badge a une place
		if is_place_dispo(place)==1: # si la place est dispo
			while c<get_autorized_badges('size', 0):
				if place==get_autorized_badges('place', c):
					set_checking_var("bm_notific", "La place N°"+str(place)+" est déjà occupé par le code "+get_autorized_badges('code', c)+".")
					c = len(listcode)
					d = 1
				c += 1
		else:
			set_checking_var("bm_notific", "La place N°"+str(place)+" doit être libre pour pour effectuer cette action.")
			d = 1

	if d==0:
		a = 0
		b = 0
		while a<get_autorized_badges('size', 0): # --------------------------- UPDATE ---------------------------
			if code==get_autorized_badges('code', a): # si le code existe deja

				listcode[a] = (len(listcode)-1, code, dateheure, place)
				iud_badge(1, code, dateheure, place)
				b = 1
				a = len(listcode)

				if place=="": # place non reservé
					if code in place_codes: # enleve le lien du badge avec une place
						envoyer('w'+str(code)+str(place_codes.index(code)))
						set_checking_var("bm_notific", "Le code "+str(code)+" n'est plus lié a la place N°"+str(place_codes.index(code))+".")
						set_place_predef(place_codes.index(code), 0, code)
					else: # on ne fait rien
						set_checking_var("bm_notific", "Le code "+str(code)+" a été mis à jour.")
				else: # place reservé
					if code in place_codes: # enleve le lien du badge avec une place
						envoyer('w'+str(code)+str(place_codes.index(code)))
						set_place_predef(place_codes.index(code), 0, code)
					envoyer('W'+str(code)+str(place))
					set_checking_var("bm_notific", "Le code "+str(code)+" a été mis à jour et lié à la place N°"+str(place)+".")
					set_place_predef(place, 1, code)
			a += 1
		if b == 0: # --------------------------- INSERT ---------------------------
			listcode.append((len(listcode), code, dateheure, place))
			iud_badge(0, code, dateheure, place)
			if place=="":
				envoyer('Z'+str(code))
				set_checking_var("bm_notific", "Le code "+str(code)+" a été ajouté.")
			else:
				envoyer('W'+str(code)+str(place))
				set_place_predef(place, 1, code)
				set_checking_var("bm_notific", "Le code "+str(code)+" a été ajouté et lié à la place N°"+str(place)+".")

	last_seconde = time.strftime('%H:%M:%S')

def del_autorized_badges(code, id):
	global last_seconde
	global listcode
	if get_autorized_badges('place', id)!="": # si place predef
		envoyer('w'+str(code)+str(get_autorized_badges('place', id)))
		set_place_predef(get_autorized_badges('place', id), 0, '')
	envoyer('z'+code)
	if id<get_autorized_badges('size', 0): # resolution d'un bug de suppression quand double clic sur croix de suppression
		listcode.remove(listcode[id])
	iud_badge(2, code)
	last_seconde = time.strftime('%H:%M:%S')

def logutilisation(par, id):
	if par=='place':
		return(logutilisations[id][4])
	elif par=='code':
		return(logutilisations[id][1])
	elif par=='dateheure':
		return(logutilisations[id][5])
	elif par=='entrantsortant':
		return(logutilisations[id][3])
	elif par=='etat':
		return(logutilisations[id][2])
	elif par=='id':
		return(logutilisations[id][0])
	elif par=='size':
		return(logsize)
	elif par=="nbpage":
		return(ceil(logsize)/17)
	elif par=="seconde":
		return(last_seconde)

'''
------------------------------------------------------
base de donnees
'''

listplaces = [(0, '', 1, 0, 1), (1, '', 1, 0, 1), (2, '', 1, 0, 1), (3, '', 1, 0, 1), (4, '', 1, 0, 1), (5, '', 1, 0, 1), (6, '', 1, 0, 1), (7, '', 1, 0, 1), (8, '', 1, 0, 1), (9, '', 1, 0, 1), (10, '', 1, 0, 1), (11, '', 1, 0, 1), (12, '', 1, 0, 1), (13, '', 1, 0, 1), (14, '', 1, 0, 1)]
listutilisation = [(1, '0000000000', 0, 2, 15), (2, '0000000000', 0, 2, 15), (3, '0000000000', 0, 2, 15), (4, '0000000000', 0, 2, 15), (5, '0000000000', 0, 2, 15), (6, '0000000000', 0, 2, 15), (7, '0000000000', 0, 2, 15), (8, '0000000000', 0, 2, 15), (9, '0000000000', 0, 2, 15), (10, '0000000000', 0, 2, 15)]
listcode = []
connexion = None
cursor = None

def load_database():
	
	global connexion
	global cursor

	connexion = sqlite3.connect('data/donnees/database.db', check_same_thread = False, isolation_level = None) # arguments utile pour passer a travers les threads
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

	connexion.commit()
	#cursor.execute("DELETE FROM badges")
	#connexion.commit()
	load_places()
	load_utilisation()
	load_badge()

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
		a += 1

def load_utilisation():
	cursor.execute("SELECT * FROM utilisation ORDER BY utilisation_id DESC LIMIT 10")
	global listutilisation
	listutilisation = cursor.fetchall() 
	a = 9
	while a>-1:
		add_last_places(listutilisation[a][4], listutilisation[a][1], listutilisation[a][3], listutilisation[a][2], listutilisation[a][5], 1)
		a -= 1

def update_place(place, code, dispo, predef, active):
	cursor.execute("UPDATE places SET places_code = ?, places_dispo = ?, places_predef = ?, places_active = ? WHERE places_id = ?", (code, dispo, predef, active, place, ))
	connexion.commit()

def insert_utilisation(code, accept, entrantsortant, place, dateheure):
	cursor.execute("INSERT INTO utilisation(utilisation_code, utilisation_accept, utilisation_entrantsortant, utilisation_place, utilisation_dateheure) VALUES(?,?,?,?,?)", (code, accept, entrantsortant, place, dateheure))
	connexion.commit()

def load_badge():
	cursor.execute("SELECT * FROM badges WHERE badges_active=1")
	global listcode
	listcode = cursor.fetchall()

def iud_badge(command, code=0, dateheure=0, place=0):
	if command==0:
		cursor.execute("INSERT INTO badges(badges_code, badges_dateheure, badges_place, badges_active) VALUES(?,?,?,?)", (code, dateheure, place, 1))
	elif command==1:
		cursor.execute("UPDATE badges SET badges_dateheure = ?, badges_place = ?, badges_active = ? WHERE badges_code = ? and badges_active = ? ", (dateheure, place, 1, code, 1))
	elif command==2:
		cursor.execute("UPDATE badges SET badges_active = ? WHERE badges_code = ? and badges_active = ?", (0, code, 1))
		#cursor.execute("DELETE FROM badges WHERE badges_code = ?", (code))
	
	connexion.commit()

def load_logutilisation(page, par=0):
	global last_seconde
	global logsize
	global logutilisations
	last_seconde = time.strftime('%H:%M:%S')
	pages = page*17
	if par==0:
		cursor.execute("SELECT Count(*) FROM utilisation")
		logsiz = cursor.fetchall() 
		logsize = logsiz[0][0]
		cursor.execute("SELECT * FROM utilisation ORDER BY utilisation_id DESC LIMIT 18 OFFSET ?", [pages])
		logutilisations = cursor.fetchall() 
	else:	
		connexion_thread = sqlite3.connect('data/donnees/database.db', check_same_thread = False, isolation_level = None)
		cursor_thread = connexion_thread.cursor()
		cursor_thread.execute("SELECT Count(*) FROM utilisation")
		logsiz = cursor_thread.fetchall() 
		logsize = logsiz[0][0]
		cursor_thread.execute("SELECT * FROM utilisation ORDER BY utilisation_id DESC LIMIT 18 OFFSET ?", [pages])
		logutilisations = cursor_thread.fetchall() 
		connexion_thread.close()
	'''
	cursor.execute("SELECT * FROM utilisation")
	hg = cursor.fetchall() 
	a = 0
	while a<logsize:
		print(hg[a])
		a += 1'''

'''
------------------------------------------------------
checking_var
'''

def set_checking_var(name, var):
	global checking_var
	checking_var[name] = var

def get_checking_var(name):
	return(checking_var[name])