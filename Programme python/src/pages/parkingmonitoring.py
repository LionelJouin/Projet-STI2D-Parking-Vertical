import os
import time

from tkinter import * 
from src.style.funct import *

# parkingmonitoring pm

pm_rectangle = []
pm_text = []
pm_rect = []
pm_code = []
pm_leg_rect = []
pm_leg_text = []
pm_leg_nb = []
pm_listbox_rect = []
pm_listbox_code = []
pm_listbox_date = []
pm_listbox_entr = []
pm_listbox_plac = []
nb_places_text = 0
pm_parking_x = 5
pm_parking_y = 5
pm_listbox_x = 5
pm_listbox_y = 330


def pm_init(box):
	#pm_createbloc(box , 1, 5, 5)
	set_checking_var("pm_p_active", places_active().count(0))
	set_checking_var("pm_p_dispo", places_dispo().count(0))
	set_checking_var("seconde", last_places('seconde', 0))

	global pm_rectangle
	global pm_text
	global pm_rect
	global pm_code
	global pm_leg_rect
	global pm_leg_text
	global pm_leg_nb
	global pm_listbox_rect
	global pm_listbox_code
	global pm_listbox_date
	global pm_listbox_entr
	global pm_listbox_plac
	pm_rectangle = []
	pm_text = []
	pm_rect = []
	pm_code = []
	pm_leg_rect = []
	pm_leg_text = []
	pm_leg_nb = []
	pm_listbox_rect = []
	pm_listbox_code = []
	pm_listbox_date = []
	pm_listbox_entr = []
	pm_listbox_plac = []

	pm_createparking(box, pm_parking_x, pm_parking_y)

	#nb_places = places_active().count(0)+places_dispo().count(0)+places_predef().count(1)
	nb_places = places_active().count(0)+places_dispo().count(0)
	nb_places = 15-nb_places

	# legende parking
	pm_createlegende(box, "#2ecc71", "Places disponibles", 380, 5, nb_places)
	pm_createlegende(box, "#e74c3c", "Places occupées", 380, 5+29, places_dispo().count(0))
	pm_createlegende(box, "#333333", "Places desactivées", 380, 5+29*2, places_active().count(0))
	pm_createlegende(box, "#3498db", "Places prédéfinies", 380, 5+29*3, places_predef().count(1))

	# legendre listbox
	pm_createlegende(box, "#C8E6C9", "Codes acceptées", 380, 355)
	pm_createlegende(box, "#FFCDD2", "Codes refusées", 380, 355+29)
	pm_createlegende(box, "#9b59b6", "Voitures entrantes", 380, 355+29*2)
	pm_createlegende(box, "#f1c40f", "Voitures sortantes", 380, 355+29*3)

	box.create_text(pm_listbox_x, pm_listbox_y, text="Derniers codes :", fill="#333333", font="Arial 15 bold", anchor=NW)
	pm_createlistbox(box, pm_listbox_x, pm_listbox_y)


def pm_createlegende(box, color, text, x, y, nb=-1):
	pm_leg_text.append(box.create_text(x+24+6, y+12, text=text, fill="#333333", font="Arial 12 bold", anchor=W))
	pm_leg_rect.append(box.create_rectangle(x, y, x+24, y+24, width=0, fill=color))
	if nb>=0 and nb<=15:
		pm_leg_nb.append(box.create_text(x+12, y+12, text=nb, fill="#ecf0f1", font="Arial 12 bold"))

def pm_updatelegende(box):
	#nb_places = places_active().count(0)+places_dispo().count(0)+places_predef().count(1)
	nb_places = places_active().count(0)+places_dispo().count(0)
	nb_places = 15-nb_places
	box.itemconfigure(pm_leg_nb[0], text=nb_places)
	box.itemconfigure(pm_leg_nb[1], text=places_dispo().count(0))
	box.itemconfigure(pm_leg_nb[2], text=places_active().count(0))
	box.itemconfigure(pm_leg_nb[3], text=places_predef().count(1))

'''
--------------------------------------------------------------------------------------
Parking
'''
def pm_createparking(box, pos_x, pos_y):
	y = pos_y+260
	id = 0
	while id<15:
		if id%3==0:
			x = pos_x
			if id>0:
				y = y-65
		elif id%3==1:
			x = pos_x+125
		elif id%3==2:
			x = pos_x+250
		pm_createbloc(box , id, x, y)
		id += 1

def pm_updateparking(box):
	id = 0
	while id<15:
		if is_place_active(id) == 0: # si la place est desactivé 	
			box.itemconfigure(pm_rectangle[id], fill='#333333')
			box.itemconfigure(pm_code[id], text=place_code(id), fill="#ecf0f1")
			box.itemconfigure(pm_text[id], fill="#ecf0f1")
		elif is_place_predef(id) == 1: # si la place est predefinie
			box.itemconfigure(pm_rectangle[id], fill='#3498db')
			if is_place_dispo(id) == 0: # si la place est occupé
				box.itemconfigure(pm_code[id], text=place_code(id), fill="#e74c3c")
				box.itemconfigure(pm_text[id], fill="#e74c3c")
			else: # si la place est libre
				box.itemconfigure(pm_code[id], text=place_code(id), fill="#ecf0f1")
				box.itemconfigure(pm_text[id], fill="#ecf0f1")
		else: # si la place est activé
			if is_place_dispo(id) == 0: # si la place est occupé
				box.itemconfigure(pm_rectangle[id], fill='#e74c3c')
				box.itemconfigure(pm_code[id], text=place_code(id), fill="#ecf0f1")
				box.itemconfigure(pm_text[id], fill="#ecf0f1")
			else: # si la place est libre
				box.itemconfigure(pm_rectangle[id], fill='#2ecc71')
				box.itemconfigure(pm_code[id], text=place_code(id), fill="#ecf0f1")
				box.itemconfigure(pm_text[id], fill="#ecf0f1")
		id += 1

def pm_createbloc(box , id, x, y):
	global pm_rectangle
	global pm_text
	global pm_rect
	pm_calculx = x+120
	pm_calculy = y+60
	if is_place_active(id) == 0: # si la place est desactivé 
		pm_rectangle.append(box.create_rectangle(x, y, pm_calculx, pm_calculy, fill='#333333', width=0))
		pm_text.append(box.create_text(x+60, y+30, text=id, fill="#ecf0f1", font="Arial 18 bold"))
		pm_code.append(box.create_text(x+60, pm_calculy, text=place_code(id), fill="#ecf0f1", font="Arial 8",anchor=S))
	elif is_place_predef(id) == 1: # si la place est predefinie
		pm_rectangle.append(box.create_rectangle(x, y, pm_calculx, pm_calculy, fill='#3498db', width=0))
		if is_place_dispo(id) == 0: # si la place est occupé
			pm_text.append(box.create_text(x+60, y+30, text=id, fill="#e74c3c", font="Arial 18 bold"))
			pm_code.append(box.create_text(x+60, pm_calculy, text=place_code(id), fill="#e74c3c", font="Arial 8",anchor=S))
		else: # si la place est libre
			pm_text.append(box.create_text(x+60, y+30, text=id, fill="#ecf0f1", font="Arial 18 bold"))
			pm_code.append(box.create_text(x+60, pm_calculy, text=place_code(id), fill="#ecf0f1", font="Arial 8",anchor=S))
	else: # si la place est activé
		if is_place_dispo(id) == 0: # si la place est occupé
			pm_rectangle.append(box.create_rectangle(x, y, pm_calculx, pm_calculy, fill='#e74c3c', width=0))
			pm_text.append(box.create_text(x+60, y+30, text=id, fill="#ecf0f1", font="Arial 18 bold"))
			pm_code.append(box.create_text(x+60, pm_calculy, text=place_code(id), fill="#ecf0f1", font="Arial 8",anchor=S))
		else: # si la place est libre
			pm_rectangle.append(box.create_rectangle(x, y, pm_calculx, pm_calculy, fill='#2ecc71', width=0))
			pm_text.append(box.create_text(x+60, y+30, text=id, fill="#ecf0f1", font="Arial 18 bold"))
			pm_code.append(box.create_text(x+60, pm_calculy, text=place_code(id), fill="#ecf0f1", font="Arial 8",anchor=S))
	pm_rect.append(box.create_rectangle(x, y, pm_calculx, pm_calculy, width=0))

	box.tag_bind(pm_rect[id], '<Enter>', lambda event, box=box, id=id: pm_onObjectOver(box, id)) 
	box.tag_bind(pm_rect[id], '<Leave>', lambda event, box=box, id=id: pm_onObjectOutOver(box, id)) 
	box.tag_bind(pm_rect[id], '<ButtonRelease-1>', lambda event, box=box, id=id: pm_onObjectClick(box, id)) 

def pm_onObjectOver(box, id):
	if is_place_active(id) == 0: # si la place est desactivé 
		box.itemconfigure(pm_rectangle[id], fill='#212121')
	elif is_place_predef(id) == 1: # si la place est desactivé 
		box.itemconfigure(pm_rectangle[id], fill='#2980b9')
	else: # si la place est activé
		if is_place_dispo(id) == 0: # si la place est occupé
			box.itemconfigure(pm_rectangle[id], fill='#c0392b')
		else: # si la place est libre
			box.itemconfigure(pm_rectangle[id], fill='#27ae60')
	box.itemconfigure(pm_text[id])
		
def pm_onObjectOutOver(box, id):
	if is_place_active(id) == 0: # si la place est desactivé 
		box.itemconfigure(pm_rectangle[id], fill='#333333')
	elif is_place_predef(id) == 1: # si la place est desactivé 
		box.itemconfigure(pm_rectangle[id], fill='#3498db')
	else: # si la place est activé
		if is_place_dispo(id) == 0: # si la place est occupé
			box.itemconfigure(pm_rectangle[id], fill='#e74c3c')
		else: # si la place est libre
			box.itemconfigure(pm_rectangle[id], fill='#2ecc71')
	box.itemconfigure(pm_text[id])	

def pm_onObjectClick(box, id):
	if is_place_active(id) == 0: # si la place est desactivé 
		set_place_active(id, 1)
		box.itemconfigure(pm_rectangle[id], fill='#2ecc71')
	elif is_place_predef(id) == 1: # si la place est desactivé 
		box.itemconfigure(pm_rectangle[id])
	else: # si la place est activé
		if is_place_dispo(id) == 0: # si la place est occupé
			box.itemconfigure(pm_rectangle[id])
		else: # si la place est libre
			set_place_active(id, 0)
			box.itemconfigure(pm_rectangle[id], fill='#333333')
	box.itemconfigure(pm_text[id])

'''
--------------------------------------------------------------------------------------
Listbox
'''
def pm_createlistbox(box, x, y):
	y += 25
	a = 0
	while a<10:
		if last_places('etat', a)==1:
			pm_listbox_rect.append(box.create_rectangle(x, y+20*a, x+370, y+20+20*a, width=0, fill='#C8E6C9'))
		else:
			pm_listbox_rect.append(box.create_rectangle(x, y+20*a, x+370, y+20+20*a, width=0, fill='#FFCDD2'))
		if last_places('entrantsortant', a)==0:
			pm_listbox_entr.append(box.create_rectangle(x+350, y+20*a, x+370, y+20+20*a, width=0, fill='#9b59b6'))
			pm_listbox_plac.append(box.create_text(x+360, y+10+20*a, text=last_places('place', a), fill="#ecf0f1", font="Arial 10 bold"))
		elif last_places('entrantsortant', a)==1:
			pm_listbox_entr.append(box.create_rectangle(x+350, y+20*a, x+370, y+20+20*a, width=0, fill='#f1c40f'))
			pm_listbox_plac.append(box.create_text(x+360, y+10+20*a, text=last_places('place', a), fill="#ecf0f1", font="Arial 10 bold"))
		else:
			pm_listbox_entr.append(box.create_rectangle(x+350, y+20*a, x+370, y+20+20*a, width=0, fill='#FFCDD2'))
			pm_listbox_plac.append(box.create_text(x+360, y+10+20*a, text=last_places('place', a), fill="#FFCDD2", font="Arial 10 bold"))
		pm_listbox_date.append(box.create_text(91, y+10+20*a, text=last_places('dateheure', a), fill="#333333", font="Arial 10"))
		pm_listbox_code.append(box.create_text(274, y+10+20*a, text=last_places('code', a), fill="#333333", font="Arial 10"))
		a += 1

def pm_updatelistbox(box):
	a = 0
	while a<10:
		if last_places('etat', a)==1:
			box.itemconfigure(pm_listbox_rect[a], fill='#C8E6C9')
		else:
			box.itemconfigure(pm_listbox_rect[a], fill='#FFCDD2')
		if last_places('entrantsortant', a)==0:
			box.itemconfigure(pm_listbox_entr[a], fill='#9b59b6')
			box.itemconfigure(pm_listbox_plac[a],  text=last_places('place', a), fill="#ecf0f1", font="Arial 10 bold")
		elif last_places('entrantsortant', a)==1:
			box.itemconfigure(pm_listbox_entr[a], fill='#f1c40f')
			box.itemconfigure(pm_listbox_plac[a],  text=last_places('place', a), fill="#ecf0f1", font="Arial 10 bold")
		else:
			box.itemconfigure(pm_listbox_entr[a], fill='#FFCDD2')
			box.itemconfigure(pm_listbox_plac[a],  text=last_places('place', a), fill="#FFCDD2", font="Arial 10 bold")
		box.itemconfigure(pm_listbox_date[a], text=last_places('dateheure', a))
		box.itemconfigure(pm_listbox_code[a], text=last_places('code', a))
		a += 1

'''
--------------------------------------------------------------------------------------
update
'''
def pm_update(box, command=1):
	#if places_active in locals() & places_dispo in locals():
	if command==1:
		if (get_checking_var("pm_p_active") or get_checking_var("pm_p_dispo") or get_checking_var("seconde")) != None:
			if get_checking_var('pm_p_active')!=places_active().count(0): # update des places actives
				set_checking_var('pm_p_active', places_active().count(0))
				time.sleep(0.1)
				pm_updatelegende(box)
			if get_checking_var('pm_p_dispo')!=places_dispo().count(0): # update des places dispo
				set_checking_var('pm_p_dispo', places_dispo().count(0))
				time.sleep(0.1)
				pm_updatelegende(box)
				pm_updateparking(box)
			if get_checking_var('seconde')!=last_places('seconde', 0): # update de la listbox
				set_checking_var("seconde", last_places('seconde', 0))
				time.sleep(0.1)
				pm_updatelistbox(box)
		else:
			set_checking_var("pm_p_active", places_active().count(0))
			set_checking_var("pm_p_dispo", places_dispo().count(0))
			set_checking_var("seconde", last_places('seconde', 0))
	else:
		pass

'''
--------------------------------------------------------------------------------------
delete
'''
def pm_delete(box):
	pass