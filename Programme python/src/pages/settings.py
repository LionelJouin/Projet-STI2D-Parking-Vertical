import os

from tkinter import * 
from tkinter.colorchooser import *

set_menu_rectangle = []
set_menu_text = []
set_menu_rect = []
set_menu_line = []
set_button_rectangle = []
set_button_text = []
set_button_rect = []
set_button_bind = []

set_selected_menu = 1

def set_init(box):
	global set_menu_rectangle
	global set_menu_text
	global set_menu_rect
	global set_menu_line
	global set_button_rectangle
	global set_button_text
	global set_button_rect
	global set_selected_menu
	global set_button_bind
	set_menu_rectangle = []
	set_menu_text = []
	set_menu_rect = []
	set_menu_line = []
	set_button_rectangle = []
	set_button_text = []
	set_button_rect = []
	set_button_bind = []
	set_selected_menu = 1


	set_createmenu(box, 0, 0, "Couleurs")
	set_createmenu(box, 1, 1, "Entête")
	set_createmenu(box, 2, 1, "Menu")
	set_createmenu(box, 3, 1, "Sous-menu")
	set_createmenu(box, 4, 1, "Contenu")
	set_createmenu(box, 5, 1, "Pied")
	set_createmenu(box, 6, 1, "Prédéfinies")
	set_createmenu(box, 7, 0, "Autres")

	set_createcontent(box, set_selected_menu)

def set_createmenu(box, id, style, text):
	calcul = (30+1)*id
	if id==set_selected_menu:
		set_menu_rectangle.append(box.create_rectangle(0, 0+calcul, 130, 30+calcul, fill='#afb5b8', width=0))
	else:
		set_menu_rectangle.append(box.create_rectangle(0, 0+calcul, 130, 30+calcul, fill='#bdc3c7', width=0))
	if style==0:
		set_menu_text.append(box.create_text(5, 15+calcul, text=text, fill="#333333", font="Arial 15 bold", anchor=W))
	else:
		set_menu_text.append(box.create_text(5, 15+calcul, text=text, fill="#333333", font="Arial 13", anchor=W))
	set_menu_line.append(box.create_line(0,30+calcul,130,30+calcul, fill='#a6abae'))
	set_menu_rect.append(box.create_rectangle(0, 0+calcul, 130, 30+calcul, width=0))

	box.tag_bind(set_menu_rect[id], '<Enter>', lambda event, box=box, id=id, style=style: set_menuOver(box, id, style)) 
	box.tag_bind(set_menu_rect[id], '<Leave>', lambda event, box=box, id=id, style=style: set_menuOutOver(box, id, style)) 
	box.tag_bind(set_menu_rect[id], '<ButtonRelease-1>', lambda event, box=box, id=id, style=style: set_menuClick(box, id, style)) 

def set_menuOver(box, id, style):
	if style==0:
		box.itemconfigure(set_menu_rectangle[id], fill='#bdc3c7')
	else:
		box.itemconfigure(set_menu_rectangle[id], fill='#afb5b8')

def set_menuOutOver(box, id, style):
	if style==0:
		box.itemconfigure(set_menu_rectangle[id], fill='#bdc3c7')
	else:
		if id==set_selected_menu:
			pass
		else:
			box.itemconfigure(set_menu_rectangle[id], fill='#bdc3c7')

def set_menuClick(box, id, style):
	if style==0:
		pass
	else:
		global set_selected_menu
		box.itemconfigure(set_menu_rectangle[set_selected_menu], fill='#bdc3c7')
		set_selected_menu = id
		box.itemconfigure(set_menu_rectangle[id], fill='#afb5b8')
		set_createcontent(box, set_selected_menu)


def set_createcontent(box, id):
	set_contentclear(box)
	if id==1:
		set_createbutton(box, 0, "color_header", "Fond de l'entête", "#292929")
		set_createbutton(box, 1, "color_text", "Texte de l'entête", "#ecf0f1")
	elif id==2:
		set_createbutton(box, 0, "color_menu", "Fond du menu", "#333333")
		set_createbutton(box, 1, "color_menu_button", "Bouton du menu", "#333333")
		set_createbutton(box, 2, "color_menu_button_select", "Bouton sélectionné du  menu", "#2ecc71")
		set_createbutton(box, 3, "color_menu_button_over", "Bouton survolé du menu", "#1C1C1C")
		set_createbutton(box, 4, "color_menu_text", "Texte du menu", "#ecf0f1")
	elif id==3:
		set_createbutton(box, 0, "color_submenu", "Fond du sous-menu", "#bdc3c7")
		set_createbutton(box, 1, "color_submenu_button", "Bouton du sous-menu", "#bdc3c7")
		set_createbutton(box, 2, "color_submenu_button_select", "Bouton sélectionné du sous-menu", "#afb5b8")
		set_createbutton(box, 3, "color_submenu_button_over", "Bouton survolé du sous-menu", "#afb5b8")
		set_createbutton(box, 4, "color_submenu_text", "Texte du sous-menu", "#333333")
	elif id==4:
		set_createbutton(box, 0, "color_content", "Fond du contenu", "#ecf0f1")
		set_createbutton(box, 1, "color_dispo", "Places disponnibles", "#2ecc71")
		set_createbutton(box, 2, "color_dispo_over", "Places disponnibles survole", "#27ae60")
		set_createbutton(box, 3, "color_occup", "Places occupées", "#e74c3c")
		set_createbutton(box, 4, "color_occup_over", "Places occupées survole", "#c0392b")
		set_createbutton(box, 5, "color_desac", "Places desactivées", "#333333")
		set_createbutton(box, 6, "color_desac_over", "Places desactivées survole", "#212121")
		set_createbutton(box, 7, "color_predef", "Places prédéfinies", "#3498db")
		set_createbutton(box, 8, "color_predef_over", "Places prédéfinies survole", "#2980b9")
		set_createbutton(box, 9, "color_accep", "Code acceptées", "#C8E6C9")
		set_createbutton(box, 10, "color_refus", "Codes refusées", "#FFCDD2")
		set_createbutton(box, 11, "color_entran", "Voitures entrantes", "#9b59b6")
		set_createbutton(box, 12, "color_sortan", "Voitures sortantes", "#f1c40f")
	elif id==5:
		set_createbutton(box, 0, "color_footer", "Fond du Pied de page", "#292929")
		set_createbutton(box, 1, "color_footer_text", "Texte du Pied de page", "#bdc3c7")
	elif id==6:
		pass

def set_createbutton(box, id, iddb, text, style):
	calcul = (20+5)*id+5
	set_button_rectangle.append(box.create_rectangle(135, calcul, 155, calcul+20, fill=style))
	set_button_text.append(box.create_text(160, calcul+10, text=text, fill="#333333", font="Arial 13", anchor=W))
	set_button_rect.append(box.create_rectangle(135, calcul, 155, calcul+20, width=0))

	set_button_bind.append(box.tag_bind(set_button_rect[id], '<ButtonRelease-1>', lambda event, box=box, id=id: set_buttonClick(box, id)))

def set_buttonClick(box, id):
    color = askcolor()
    print(color)

def set_contentclear(box):
	global set_button_rectangle
	global set_button_text
	global set_button_rect
	global set_button_bind
	a = 0
	while a<len(set_button_rectangle):
		box.delete(set_button_rectangle[a])
		box.delete(set_button_text[a])
		box.delete(set_button_rect[a])
		box.unbind("<ButtonRelease-1>", set_button_bind[a])
		a += 1
	set_button_rectangle = []
	set_button_text = []
	set_button_rect = []
	set_button_bind = []

'''
--------------------------------------------------------------------------------------
update
'''
def set_update(box, command=1):
	if command==1:
		pass
	else:
		pass
'''

--------------------------------------------------------------------------------------
delete
'''
def set_delete(box):
	pass