import os

from tkinter import * 
from src.style.funct import *

pc_button_rectangle = []
pc_button_text = []
pc_button_rect = []
pc_dechargement_rectangle = []
pc_dechargement_text = []
pc_dechargement_code = []
pc_dechargement_place = []
pc_dechargement_line = []
pc_dechargement_rect = []

def pc_init(box):

	set_checking_var("pm_p_dispo", places_dispo().count(0))
	set_checking_var("seconde", last_places('seconde', 0))

	global pc_button_rectangle
	global pc_button_text
	global pc_button_rect
	global pc_dechargement_rectangle
	global pc_dechargement_text
	global pc_dechargement_code
	global pc_dechargement_place
	global pc_dechargement_line
	global pc_dechargement_rect
	pc_button_rectangle = []
	pc_button_text = []
	pc_button_rect = []
	pc_dechargement_rectangle = []
	pc_dechargement_text = []
	pc_dechargement_code = []
	pc_dechargement_place = []
	pc_dechargement_line = []
	pc_dechargement_rect = []

	pc_createbutton(box, 5, 5, 0, "Redémarrer le système", 0)
	pc_createbutton(box, 260, 5, 1, "Désactiver le système", 1)

	pc_createlistdecharg(box, 5, 45)
	
def pc_createbutton(box, x, y, id, text, style):
	if style==0:
		pc_button_rectangle.append(box.create_rectangle(x, y, x+250, y+35, fill='#212121', width=0))
	elif style==1:
		pc_button_rectangle.append(box.create_rectangle(x, y, x+250, y+35, fill='#FF5722', width=0))
	pc_button_text.append(box.create_text(x+250/2, y+34/2, text=text, fill="#ecf0f1", font="Arial 15"))
	pc_button_rect.append(box.create_rectangle(x, y, x+250, y+35, width=0))

	box.tag_bind(pc_button_rect[id], '<Enter>', lambda event, box=box, id=id, style=style: pc_buttonOver(box, id, style)) 
	box.tag_bind(pc_button_rect[id], '<Leave>', lambda event, box=box, id=id, style=style: pc_buttonOutOver(box, id, style)) 
	box.tag_bind(pc_button_rect[id], '<ButtonRelease-1>', lambda event, box=box, id=id: pc_buttonClick(box, id)) 

def pc_buttonOver(box, id, style):
	if style==0:
		box.itemconfigure(pc_button_rectangle[id], fill='#424242')
	elif style==1:
		box.itemconfigure(pc_button_rectangle[id], fill='#E64A19')

def pc_buttonOutOver(box, id, style):
	if style==0:
		box.itemconfigure(pc_button_rectangle[id], fill='#212121')
	elif style==1:
		box.itemconfigure(pc_button_rectangle[id], fill='#FF5722')

def pc_buttonClick(box, id):
	if id==0:
		envoyer('r')
	elif id==1:
		pass

def pc_createblocdecharg(box, x, y, id):
	if is_place_dispo(id)==1:
		pc_dechargement_rectangle.append(box.create_rectangle(x, y, x+200, y+40, fill='#9E9E9E', width=0))
	else:
		pc_dechargement_rectangle.append(box.create_rectangle(x, y, x+200, y+40, fill='#e74c3c', width=0))
	pc_dechargement_text.append(box.create_text(x+5, y+5, text="Décharger", fill="#ecf0f1", font="Arial 13 bold", anchor="nw"))
	pc_dechargement_code.append(box.create_text(x+5, y+23, text=place_code(id), fill="#ecf0f1", font="Arial 9", anchor="nw"))
	pc_dechargement_place.append(box.create_text(x+175, y+20, text=id, fill="#ecf0f1", font="Arial 25 bold"))
	pc_dechargement_line.append(box.create_line(x+150, y, x+150, y+40, fill="white", width=1))
	pc_dechargement_rect.append(box.create_rectangle(x, y, x+200, y+40, width=0))

	box.tag_bind(pc_dechargement_rect[id], '<Enter>', lambda event, box=box, id=id: pc_blocOver(box, id)) 
	box.tag_bind(pc_dechargement_rect[id], '<Leave>', lambda event, box=box, id=id: pc_blocOutOver(box, id)) 
	box.tag_bind(pc_dechargement_rect[id], '<ButtonRelease-1>', lambda event, box=box, id=id: pc_blocClick(box, id)) 

def pc_blocOver(box, id):
	if is_place_dispo(id)==1:
		box.itemconfigure(pc_dechargement_rectangle[id], fill='#757575')
	else:
		box.itemconfigure(pc_dechargement_rectangle[id], fill='#c0392b')

def pc_blocOutOver(box, id):
	if is_place_dispo(id)==1:
		box.itemconfigure(pc_dechargement_rectangle[id], fill='#9E9E9E')
	else:
		box.itemconfigure(pc_dechargement_rectangle[id], fill='#e74c3c')

def pc_blocClick(box, id):
	if is_place_dispo(id)==1:
		pass
	else:
		if is_connectedtosystem()==1:
			envoyer("v"+str(id))
			if is_place_predef(id)==1:
				set_place_dispo(id, 1, place_code(id))
			else:
				set_place_dispo(id, 1, "")

def pc_updateblocdecharg(box, id):
	if is_place_dispo(id)==1:
		box.itemconfigure(pc_dechargement_rectangle[id], fill='#9E9E9E')
	else:
		box.itemconfigure(pc_dechargement_rectangle[id], fill='#e74c3c')
	box.itemconfigure(pc_dechargement_code[id], text=place_code(id))

def pc_createlistdecharg(box, x, y):
	a = 0
	while a<15:
		if a>7:
			pc_createblocdecharg(box, x+205, y+(40+5)*(a-8), a)
		else:
			pc_createblocdecharg(box, x, y+(40+5)*a, a)
		a += 1

def pc_updatelistdecharg(box):
	a = 0
	while a<15:
		if a>7:
			pc_updateblocdecharg(box, a)
		else:
			pc_updateblocdecharg(box, a)
		a += 1



'''
--------------------------------------------------------------------------------------
update
'''
def pc_update(box, command=1):
	if command==1:
		if (get_checking_var("pm_p_active") or get_checking_var("pm_p_dispo") or get_checking_var("seconde")) != None:
			if get_checking_var('pm_p_dispo')!=places_dispo().count(0): # update des places dispo
				set_checking_var('pm_p_dispo', places_dispo().count(0))
				time.sleep(0.1)
				pc_updatelistdecharg(box)
			if get_checking_var('seconde')!=last_places('seconde', 0): # update de la listbox
				set_checking_var("seconde", last_places('seconde', 0))
				time.sleep(0.1)
				pc_updatelistdecharg(box)
		else:
			set_checking_var("pm_p_dispo", places_dispo().count(0))
			set_checking_var("seconde", last_places('seconde', 0))
	else:
		pass
'''

--------------------------------------------------------------------------------------
delete
'''
def pc_delete(box):
	pass