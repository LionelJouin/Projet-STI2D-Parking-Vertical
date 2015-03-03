import os

from tkinter import * 

pu_tableau_rectangle = []
pu_tableau_id = []
pu_tableau_dates = []
pu_tableau_badges = []
pu_tableau_entrantsortant = []
pu_tableau_place = []
pu_tableau_etat = []
pu_legende_rectangle = []
pu_legende_text = []

pu_tableau_posx = 5
pu_tableau_posy = 63

def pu_init(box):

	global pu_tableau_rectangle
	global pu_tableau_id
	global pu_tableau_dates
	global pu_tableau_badges
	global pu_tableau_entrantsortant
	global pu_tableau_place
	global pu_tableau_etat
	global pu_legende_rectangle
	global pu_legende_text
	pu_tableau_rectangle = []
	pu_tableau_id = []
	pu_tableau_dates = []
	pu_tableau_badges = []
	pu_tableau_entrantsortant = []
	pu_tableau_place = []
	pu_tableau_etat = []
	pu_legende_rectangle = []
	pu_legende_text = []
	
	pu_createlegende(box, "#C8E6C9", "Codes acceptées", 5, 5)
	pu_createlegende(box, "#FFCDD2", "Codes refusées", 5, 34)
	pu_createlegende(box, "#9b59b6", "Voitures entrantes", 190, 5)
	pu_createlegende(box, "#f1c40f", "Voitures sortantes", 190, 34)

	pu_createline(box, pu_tableau_posx, pu_tableau_posy, 0, 'ID')
	pu_createtableau(box, pu_tableau_posx, pu_tableau_posy)

def pu_createlegende(box, color, text, x, y):
	pu_legende_text.append(box.create_text(x+24+6, y+12, text=text, fill="#333333", font="Arial 12 bold", anchor=W))
	pu_legende_rectangle.append(box.create_rectangle(x, y, x+24, y+24, width=0, fill=color))

def pu_createline(box, x, y, style, id):
	if box.winfo_width()<640:
		largeur = 640
	else :
		largeur = box.winfo_width()
	if style==0:
		pu_tableau_rectangle.append(box.create_rectangle(x, y, largeur-x*2, y+20, fill='#9E9E9E', width=0))
	elif style==1:
		pu_tableau_rectangle.append(box.create_rectangle(x, y, largeur-x*2, y+20, fill='#C8E6C9', width=0))
	elif style==2:
		pu_tableau_rectangle.append(box.create_rectangle(x, y, largeur-x*2, y+20, fill='#FFCDD2', width=0))
	pu_tableau_id.append(box.create_text(x+5, y+10, text=id, fill="#333333", font="Arial 10 bold", anchor='w'))

def pu_createtableau(box, x, y):
	a = 0
	while a<17:
		if a!=5:
			pu_createline(box, x, y+20*(a+1), 1, a)
		else:
			pu_createline(box, x, y+20*(a+1), 2, a)
		a += 1

'''
--------------------------------------------------------------------------------------
update
'''
def pu_update(box, command=1):
	if command==1:
		pass
	elif command==2: # la taille de la fenetre change
		pass
	else:
		pass
'''

--------------------------------------------------------------------------------------
delete
'''
def pu_delete(box):
	pass