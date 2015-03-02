import os

from tkinter import * 

pu_tableau_rectangle = []
pu_tableau_id = []
pu_tableau_dates = []
pu_tableau_badges = []
pu_tableau_entrantsortant = []
pu_tableau_place = []
pu_tableau_etat = []

pu_tableau_posx = 5
pu_tableau_posy = 120

def pu_init(box):

	global pu_tableau_rectangle
	global pu_tableau_id
	global pu_tableau_dates
	global pu_tableau_badges
	global pu_tableau_entrantsortant
	global pu_tableau_place
	global pu_tableau_etat
	pu_tableau_rectangle = []
	pu_tableau_id = []
	pu_tableau_dates = []
	pu_tableau_badges = []
	pu_tableau_entrantsortant = []
	pu_tableau_place = []
	pu_tableau_etat = []
	
def bm_createline(box, x, y, style, id, code, place, date, supp):
	pass

def pu_createtableau(box, x, y):
	pass

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