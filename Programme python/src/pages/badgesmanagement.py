import os
import time

from tkinter import * 
from src.style.funct import *

bm_entry = []
bm_entry_val = []
bm_label = []
bm_button_rectangle = []
bm_button_text = []
bm_button_rect = []
bm_notif_rect = []
bm_notif_text = []
bm_notific = "Aucune notification"
bm_tableau_rectangle = []
bm_tableau_id = []
bm_tableau_code = []
bm_tableau_place = []
bm_tableau_date = []
bm_tableau_del = []
bm_tableau_dela = [0]
bm_tableau_height = 0
bm_tableau_nbline = 0

bm_notif_posx = 5
bm_notif_posy = 70
bm_tableau_posx = 5
bm_tableau_posy = 120

def bm_init(box):

	set_checking_var("bm_nb_badges", get_autorized_badges('size', 1))
	set_checking_var("seconde", last_places('seconde', 0))

	global bm_entry
	global bm_entry_val
	global bm_label
	global bm_button_rectangle
	global bm_button_text
	global bm_button_rect
	global bm_notif_rect
	global bm_notif_text
	global bm_notific
	global bm_tableau_rectangle
	global bm_tableau_id
	global bm_tableau_code
	global bm_tableau_place
	global bm_tableau_date
	global bm_tableau_del
	global bm_tableau_dela
	global bm_tableau_height
	global bm_tableau_nbline
	bm_entry = []
	bm_entry_val = []
	bm_label = []
	bm_button_rectangle = []
	bm_button_text = []
	bm_button_rect = []
	bm_notif_rect = []
	bm_notif_text = []
	bm_notific = "Aucune notification"
	bm_tableau_rectangle = []
	bm_tableau_id = []
	bm_tableau_code = []
	bm_tableau_place = []
	bm_tableau_date = []
	bm_tableau_del = []
	bm_tableau_dela = [0]
	bm_tableau_height = box.winfo_height()-120
	bm_tableau_nbline = (bm_tableau_height-100)/20

	# formulaire
	bm_formulaires_a(box, 0, 5, 5)
	bm_formulaires_b(box, 1, 5, 35) # id 1 et 2
	bm_button(box, 0, 300, 5)
	bm_button(box, 1, 425, 35)

	# notification
	bm_notif(box, bm_notif_posx, bm_notif_posy)

	# tableau
	bm_createline(box, bm_tableau_posx, bm_tableau_posy+20*0, 0, "ID", "Code d'Accès", "Place", "Date et heure d'ajout", "Supprimer")
	bm_createtableau(box, bm_tableau_posx, bm_tableau_posy)


'''
--------------------------------------------------------------------------------------
formulaires et notification
'''
def bm_formulaires_a(box, id, x, y):
	global bm_entry_val
	bm_label.append(Label(box, text="Ajouter le badge : ", bd=0, fg='#333333', font="Arial 15 bold"))
	bm_label[id].place(x=x, y=y, anchor=NW)
	bm_entry_val.append(StringVar())
	bm_entry.append(Entry(box, width=10, bd=0, bg='#bdc3c7', fg='#333333', disabledbackground='#bdc3c7', disabledforeground='#333333', font="Arial 15 bold", textvariable=bm_entry_val[id]))
	bm_entry[id].place(x=x+175, y=y, anchor=NW)
	bm_entry[id].insert(0, "0000000000")


def bm_formulaires_b(box, id, x, y):
	global bm_entry_val
	bm_label.append(Label(box, text="Lier le badge : ", bd=0, fg='#333333', font="Arial 15 bold"))
	bm_label[id].place(x=x, y=y, anchor=NW)
	bm_entry_val.append(StringVar())
	bm_entry.append(Entry(box, width=10, bd=0, bg='#bdc3c7', fg='#333333', disabledbackground='#bdc3c7', disabledforeground='#333333', font="Arial 15 bold", textvariable=bm_entry_val[id]))
	bm_entry[id].place(x=x+140, y=y, anchor=NW)
	bm_entry[id].insert(0, "0000000000")

	bm_label.append(Label(box, text="à la place N° : ", bd=0, fg='#333333', font="Arial 15 bold"))
	bm_label[id+1].place(x=x+255, y=y, anchor=NW)
	bm_entry_val.append(StringVar())
	bm_entry.append(Entry(box, width=2, bd=0, bg='#bdc3c7', fg='#333333', disabledbackground='#bdc3c7', disabledforeground='#333333', font="Arial 15 bold", textvariable=bm_entry_val[id+1]))
	bm_entry[id+1].place(x=x+390, y=y, anchor=NW)
	bm_entry[id+1].insert(0, "00")

def bm_button(box, id, x, y):
	bm_button_rectangle.append(box.create_rectangle(x, y, x+30, y+26, fill='#2ecc71', width=0))
	bm_button_text.append(box.create_text(x+15, y+13, text=">", fill="#ecf0f1", font="Arial 20"))
	bm_button_rect.append(box.create_rectangle(x, y, x+30, y+25, width=0))

	box.tag_bind(bm_button_rect[id], '<Enter>', lambda event, box=box, id=id: bm_buttonOver(box, id)) 
	box.tag_bind(bm_button_rect[id], '<Leave>', lambda event, box=box, id=id: bm_buttonOutOver(box, id)) 
	box.tag_bind(bm_button_rect[id], '<ButtonRelease-1>', lambda event, box=box, id=id: bm_buttonClick(box, id))

def bm_buttonOver(box, id):
	box.itemconfigure(bm_button_rectangle[id], fill='#27ae60')

def bm_buttonOutOver(box, id):
	box.itemconfigure(bm_button_rectangle[id], fill='#2ecc71')

def bm_buttonClick(box, id):
	if id == 0:
		add_autorized_badges(bm_entry[0].get(), time.strftime('%d/%m/%Y - %H:%M'), "")
	else:
		add_autorized_badges(bm_entry[1].get(), time.strftime('%d/%m/%Y - %H:%M'), bm_entry[2].get())

def bm_notif(box, x, y):
	if box.winfo_width()<640:
		largeur = 640
	else :
		largeur = box.winfo_width()
	bm_notif_rect.append(box.create_rectangle(x, y, largeur-x*2, y+40, fill='#FFB74D', width=0))
	bm_notif_text.append(box.create_text(largeur/2, y+20, text=bm_notific, fill="#ecf0f1", font="Arial 16"))

def bm_notif_update(box):
	if box.winfo_width()>640:
		box.itemconfigure(bm_notif_text[0], text=bm_notific)
		box.coords(bm_notif_rect[0], bm_notif_posx, bm_notif_posy, box.winfo_width()-bm_notif_posx*2, bm_notif_posy+40)
		box.coords(bm_notif_text[0], box.winfo_width()/2, bm_notif_posy+20)

'''
--------------------------------------------------------------------------------------
tableau
'''
def bm_createline(box, x, y, style, id, code, place, date, supp):
	if box.winfo_width()<640:
		largeur = 640
	else :
		largeur = box.winfo_width()
	if style==0:
		bm_tableau_rectangle.append(box.create_rectangle(x, y, largeur-x*2, y+20, fill='#9E9E9E', width=0))
	elif style==1:
		bm_tableau_rectangle.append(box.create_rectangle(x, y, largeur-x*2, y+20, fill='#EEEEEE', width=0))
	elif style==2:
		bm_tableau_rectangle.append(box.create_rectangle(x, y, largeur-x*2, y+20, fill='#E0E0E0', width=0))
	else:
		pass
	bm_tableau_id.append(box.create_text(x+5, y+10, text=id, fill="#333333", font="Arial 10 bold", anchor='w'))
	bm_tableau_code.append(box.create_text(largeur*0.25, y+10, text=code, fill="#333333", font="Arial 10 bold"))
	bm_tableau_place.append(box.create_text(largeur*0.5, y+10, text=place, fill="#333333", font="Arial 10 bold"))
	bm_tableau_date.append(box.create_text(largeur*0.75, y+10, text=date, fill="#333333", font="Arial 10 bold"))
	bm_tableau_del.append(box.create_text(largeur-50, y+10, text=supp, fill="#333333", font="Arial 10 bold"))
	if id!='ID':
		bm_tableau_dela.append(box.tag_bind(bm_tableau_del[id+1], '<ButtonRelease-1>', lambda event, box=box, id=code: bm_delClick(box, code)))

def bm_updateline(box, style, id, code, place, date, supp):
	if style==0:
		box.itemconfigure(bm_tableau_rectangle[id+1], fill='#9E9E9E', width=0)
	elif style==1:
		box.itemconfigure(bm_tableau_rectangle[id+1], fill='#EEEEEE', width=0)
	elif style==2:
		box.itemconfigure(bm_tableau_rectangle[id+1], fill='#E0E0E0', width=0)
	else:
		pass
	box.itemconfigure(bm_tableau_id[id+1], text=id)
	box.itemconfigure(bm_tableau_code[id+1], text=code)
	box.itemconfigure(bm_tableau_place[id+1], text=place)
	box.itemconfigure(bm_tableau_date[id+1], text=date)
	box.itemconfigure(bm_tableau_del[id+1], text=supp)

def bm_deleteline(box, id):
	print(id)
	#box.delete(bm_tableau_rectangle[id+1])
	#box.delete(bm_tableau_id[id+1])
	#box.delete(bm_tableau_code[id+1])
	#box.delete(bm_tableau_place[id+1])
	#box.delete(bm_tableau_date[id+1])
	#box.delete(bm_tableau_del[id+1])
	#box.unbind("<ButtonRelease-1>", bm_tableau_del[id+1])
	box.delete(bm_tableau_rectangle[id])
	box.delete(bm_tableau_id[id])
	box.delete(bm_tableau_code[id])
	box.delete(bm_tableau_place[id])
	box.delete(bm_tableau_date[id])
	box.delete(bm_tableau_del[id])
	box.unbind("<ButtonRelease-1>", bm_tableau_dela[id])
	del bm_tableau_rectangle[-1]
	del bm_tableau_id[-1]
	del bm_tableau_code[-1]
	del bm_tableau_place[-1]
	del bm_tableau_date[-1]
	del bm_tableau_del[-1]

def bm_delClick(box, code):
	del_autorized_badges(code)

def bm_createtableau(box, x, y):
	a = 0
	#while a<bm_tableau_nbline:
	while a<get_autorized_badges('size', 1):
		if a%2==0:
			bm_createline(box, x, y+20*(a+1), 1, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
		else:
			bm_createline(box, x, y+20*(a+1), 2, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
		a += 1

def bm_updatedatatableau(box):
	print(get_checking_var("bm_nb_badges"))
	if get_checking_var("bm_nb_badges")<get_autorized_badges('size', 1): # insert
		print('a')
		a = get_checking_var("bm_nb_badges")
		while a<get_autorized_badges('size', 1):
			bm_createline(box, bm_tableau_posx, bm_tableau_posy+20*(a+1), 1, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
			a += 1
	elif get_checking_var("bm_nb_badges")>=get_autorized_badges('size', 1): # delete
		print('b')
		print( str(get_checking_var("bm_nb_badges"))+' | '+str(get_autorized_badges('size', 1)) )
		a = get_checking_var("bm_nb_badges")
		while a>=get_autorized_badges('size', 1): 
			bm_deleteline(box, a)
			a -= 1
		a = 0
		while a<get_autorized_badges('size', 1):
			bm_updateline(box, 2, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
			a += 1
	else: # update
		print('c')
		a = 0
		while a<get_autorized_badges('size', 1):
			bm_updateline(box, 2, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
			a += 1
	'''
	a = 0
	#print(get_autorized_badges('size', 1))
	while a<get_autorized_badges('size', 1):
		if a%2==0:
			if a>=len(bm_tableau_del)-1: # create
				bm_createline(box, bm_tableau_posx, bm_tableau_posy+20*(a+1), 1, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
			#elif a<len(bm_tableau_del)-1:
			#	bm_deleteline(box, a)
			else: # update
				bm_updateline(box, 1, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
		else:
			if a>=len(bm_tableau_del)-1: # create
				bm_createline(box, bm_tableau_posx, bm_tableau_posy+20*(a+1), 2, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
			#elif a<len(bm_tableau_del)-1:
			#	bm_deleteline(box, a)
			else: # update
				bm_updateline(box, 2, a, get_autorized_badges('code', a), get_autorized_badges('place', a), get_autorized_badges('dateheure', a), "X")
		a += 1
	'''

def bm_updatetableau(box):
	'''
	global bm_tableau_height
	global bm_tableau_nbline
	tabheight = bm_tableau_height
	nbline = bm_tableau_nbline
	bm_tableau_height = box.winfo_height()-120
	bm_tableau_nbline = (bm_tableau_height-100)/20

	if tabheight>bm_tableau_height: # on supprime des elements
		if int(nbline)>int(bm_tableau_nbline):
			deleteline(box, int(nbline)+1)
		#print(str(int(nbline))+" | "+str(int(bm_tableau_nbline)))
	elif tabheight<bm_tableau_height: # on ajoute des elements
		if int(nbline)<int(bm_tableau_nbline):
			bm_createline(box, bm_tableau_posx, bm_tableau_posy+20*(int(nbline)), 1, int(nbline)-1, "0000000000", "", "25/02/2015 - 16:57", "X")
	'''
	if box.winfo_width()>640:
		a = 0
		while a<len(bm_tableau_rectangle):
			box.coords(bm_tableau_rectangle[a], bm_tableau_posx, bm_tableau_posy+20*a, box.winfo_width()-bm_tableau_posx*2, bm_tableau_posy+20*a+20)
			box.coords(bm_tableau_id[a], bm_tableau_posx+5, bm_tableau_posy+20*a+10)
			box.coords(bm_tableau_code[a], box.winfo_width()*0.25, bm_tableau_posy+20*a+10)
			box.coords(bm_tableau_place[a], box.winfo_width()*0.5, bm_tableau_posy+20*a+10)
			box.coords(bm_tableau_date[a], box.winfo_width()*0.75, bm_tableau_posy+20*a+10)
			box.coords(bm_tableau_del[a], box.winfo_width()-50, bm_tableau_posy+20*a+10)
			a += 1


'''
--------------------------------------------------------------------------------------
update
'''
def bm_update(box, command=1):
	if command==1: # une variable change
		if get_checking_var("seconde") != None:
			if get_checking_var('seconde')!=get_autorized_badges('seconde', 0): # update de la listbox
				set_checking_var("seconde", get_autorized_badges('seconde', 0))
				bm_updatedatatableau(box)
				set_checking_var("bm_nb_badges", get_autorized_badges('size', 1))
		else:
			set_checking_var("seconde", get_autorized_badges('seconde', 0))
			set_checking_var("bm_nb_badges", get_autorized_badges('size', 1))
	elif command==2: # la taille de la fenetre change
		bm_notif_update(box)
		bm_updatetableau(box)
	else:
		pass
'''

--------------------------------------------------------------------------------------
delete
'''
def bm_delete(box):
	a = 0
	while a<len(bm_label):
		bm_label[a].destroy()
		bm_entry[a].destroy()
		a += 1