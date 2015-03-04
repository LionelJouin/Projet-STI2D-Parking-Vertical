import os

from tkinter import * 
from src.style.funct import *

pu_tableau_rectangle = []
pu_tableau_id = []
pu_tableau_dates = []
pu_tableau_badges = []
pu_tableau_entrantsortant = []
pu_tableau_place = []
pu_tableau_etat = []
pu_tableau_dateheure = []
pu_legende_rectangle = []
pu_legende_text = []
pu_pagination_rectangle = []
pu_pagination_text = []
pu_pagination_rect = []

pu_tableau_posx = 5
pu_tableau_posy = 63

def pu_init(box):

	load_logutilisation(1)

	global pu_tableau_rectangle
	global pu_tableau_id
	global pu_tableau_dates
	global pu_tableau_badges
	global pu_tableau_entrantsortant
	global pu_tableau_place
	global pu_tableau_etat
	global pu_tableau_dateheure
	global pu_legende_rectangle
	global pu_legende_text
	global pu_pagination_rectangle
	global pu_pagination_text
	global pu_pagination_rect
	pu_tableau_rectangle = []
	pu_tableau_id = []
	pu_tableau_dates = []
	pu_tableau_badges = []
	pu_tableau_entrantsortant = []
	pu_tableau_place = []
	pu_tableau_etat = []
	pu_tableau_dateheure = []
	pu_legende_rectangle = []
	pu_legende_text = []
	pu_pagination_rectangle = []
	pu_pagination_text = []
	pu_pagination_rect = []
	
	pu_createlegende(box, "#C8E6C9", "Codes acceptées", 5, 5)
	pu_createlegende(box, "#FFCDD2", "Codes refusées", 5, 34)
	pu_createlegende(box, "#9b59b6", "Voitures entrantes", 190, 5)
	pu_createlegende(box, "#f1c40f", "Voitures sortantes", 190, 34)

	pu_createline(box, pu_tableau_posx, pu_tableau_posy, 0, "ID", "Code d'accès", 2, "Place | Voiture entrante ou sortante", "04/03/2015 - 21:04")
	pu_createtableau(box, pu_tableau_posx, pu_tableau_posy)

	pu_createpagination(box,0 ,pu_tableau_posx, pu_tableau_posy+365, "<")
	pu_createpagination(box,1 ,pu_tableau_posx+35, pu_tableau_posy+365, ">")


def pu_createlegende(box, color, text, x, y):
	pu_legende_text.append(box.create_text(x+24+6, y+12, text=text, fill="#333333", font="Arial 12 bold", anchor=W))
	pu_legende_rectangle.append(box.create_rectangle(x, y, x+24, y+24, width=0, fill=color))

def pu_createline(box, x, y, style, id, badges, etrantsortant, place, dateheure):
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

	if etrantsortant==0:
		pu_tableau_etat.append(box.create_rectangle(largeur-160, y,largeur-140, y+20, fill='#9b59b6', width=0))
		pu_tableau_place.append(box.create_text(largeur-150, y+10, text=place, fill="#333333", font="Arial 10 bold"))
	elif etrantsortant==1:
		pu_tableau_etat.append(box.create_rectangle(largeur-160, y,largeur-140, y+20, fill='#f1c40f', width=0))
		pu_tableau_place.append(box.create_text(largeur-150, y+10, text=place, fill="#333333", font="Arial 10 bold"))
	elif etrantsortant==2:
		pu_tableau_etat.append(box.create_rectangle(largeur-160, y,largeur-140, y+20, fill='#9E9E9E', width=0))
		pu_tableau_place.append(box.create_text(largeur-150, y+10, text=place, fill="#333333", font="Arial 10 bold"))
	else:
		pu_tableau_etat.append(box.create_rectangle(largeur-160, y,largeur-140, y+20, fill='#FFCDD2', width=0))
		pu_tableau_place.append(box.create_text(largeur-150, y+10, text=place, fill="#FFCDD2", font="Arial 10 bold"))

	pu_tableau_id.append(box.create_text(x+5, y+10, text=id, fill="#333333", font="Arial 10 bold", anchor='w'))
	pu_tableau_badges.append(box.create_text(largeur*0.25, y+10, text=badges, fill="#333333", font="Arial 10 bold"))
	pu_tableau_dateheure.append(box.create_text(largeur*0.5, y+10, text=dateheure, fill="#333333", font="Arial 10 bold"))

def pu_createtableau(box, x, y):
	a = 0
	while a<17:
		if a!=5:
			pu_createline(box, x, y+20*(a+1), 1, a, '0000000000', 0, '8', "04/03/2015 - 21:04")
		else:
			pu_createline(box, x, y+20*(a+1), 2, a, '0000000000', 3, '8', "04/03/2015 - 21:04")
		a += 1

def pu_updatetableau(box):
	if box.winfo_width()>640:
		a = 0
		while a<len(pu_tableau_rectangle):
			box.coords(pu_tableau_rectangle[a], pu_tableau_posx, pu_tableau_posy+20*a, box.winfo_width()-pu_tableau_posx*2, pu_tableau_posy+20*a+20)
			box.coords(pu_tableau_etat[a], box.winfo_width()-160, pu_tableau_posy+20*a, box.winfo_width()-140, pu_tableau_posy+20*a+20)
			box.coords(pu_tableau_place[a], box.winfo_width()-150, pu_tableau_posy+20*a+10)
			box.coords(pu_tableau_badges[a], box.winfo_width()*0.25, pu_tableau_posy+20*a+10)
			box.coords(pu_tableau_dateheure[a], box.winfo_width()*0.5, pu_tableau_posy+20*a+10)
			a += 1

def pu_createpagination(box, id, x, y, text):
	pu_pagination_rectangle.append(box.create_rectangle(x, y, x+30, y+26, fill='#2ecc71', width=0))
	pu_pagination_text.append(box.create_text(x+15, y+13, text=text, fill="#ecf0f1", font="Arial 20"))
	pu_pagination_rect.append(box.create_rectangle(x, y, x+30, y+25, width=0))
	box.tag_bind(pu_pagination_rect[id], '<Enter>', lambda event, box=box, id=id: pu_paginationOver(box, id)) 
	box.tag_bind(pu_pagination_rect[id], '<Leave>', lambda event, box=box, id=id: pu_paginationOutOver(box, id)) 
	box.tag_bind(pu_pagination_rect[id], '<ButtonRelease-1>', lambda event, box=box, id=id: pu_paginationClick(box, id))

def pu_paginationOver(box, id):
	box.itemconfigure(pu_pagination_rectangle[id], fill='#27ae60')

def pu_paginationOutOver(box, id):
	box.itemconfigure(pu_pagination_rectangle[id], fill='#2ecc71')

'''
--------------------------------------------------------------------------------------
update
'''
def pu_update(box, command=1):
	if command==1:
		pass
	elif command==2: # la taille de la fenetre change
		pu_updatetableau(box)
	else:
		pass
'''

--------------------------------------------------------------------------------------
delete
'''
def pu_delete(box):
	pass