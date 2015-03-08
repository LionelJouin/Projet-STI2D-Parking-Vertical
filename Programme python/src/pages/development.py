import os

from tkinter import * 

dev_text = []

def dev_init(box):

	global dev_text
	dev_text = []

	dev_createtext(box, 5, 5, "Lionel Jouin", 2)
	dev_createtext(box, 5, 5*2+15*1+13*0, "Supervision", 4)
	dev_createtext(box, 5, 5*3+15*1+13*1, "Python 3.4 ( tkinter ) | Sqlite", 1)
	dev_createtext(box, 5, 5*4+15*1+13*2, "https://github.com/LionelJouin/Projet-STI2D-Parking-Vertical", 1)
	dev_createtext(box, 5, 5*5+15*1+13*3, "Justin Rouzier", 2)
	dev_createtext(box, 5, 5*6+15*2+13*3, "IHM", 4)
	dev_createtext(box, 5, 5*7+15*2+13*4, "C++ ( Qt ) | Android", 1)
	dev_createtext(box, 5, 5*8+15*2+13*5, "https://github.com/DarkInFire/projet_parking", 1)
	dev_createtext(box, 5, 5*9+15*2+13*6, "Aloïs Lardeux", 2)
	dev_createtext(box, 5, 5*10+15*3+13*6, "Gestion", 4)
	dev_createtext(box, 5, 5*11+15*3+13*7, "C | Arduino", 1)
	dev_createtext(box, 5, 5*12+15*3+13*8, "Clément Bourdais", 2)
	dev_createtext(box, 5, 5*13+15*4+13*8, "Demande d'accès", 4)
	dev_createtext(box, 5, 5*14+15*4+13*9, "C | Arduino", 1)
	dev_createtext(box, 5, 5*15+15*4+13*10, "Jean Trouillard | Adel Hanifi", 3)
	dev_createtext(box, 5, 5*16+15*5+13*10, "API", 4)
	dev_createtext(box, 5, 5*17+15*5+13*11, "TSX17 | Millenium 3", 1)
	dev_createtext(box, 5, 5*19+15*5+13*12, "Projet STI2D - SIN | EE", 0)
	dev_createtext(box, 5, 5*20+15*6+13*12, "2014 - 2015", 0)
	
def dev_createtext(box, x, y, text, style):
	if style==0:
		dev_text.append(box.create_text(x, y, text=text, fill="#333333", font="Arial 15 bold", anchor="nw"))
	elif style==1:
		dev_text.append(box.create_text(x, y, text=text, fill="#333333", font="Arial 13", anchor="nw"))
	elif style==2:
		dev_text.append(box.create_text(x, y, text=text, fill="#2ecc71", font="Arial 15 bold", anchor="nw"))
	elif style==3:
		dev_text.append(box.create_text(x, y, text=text, fill="#3498db", font="Arial 15 bold", anchor="nw"))
	elif style==4:
		dev_text.append(box.create_text(x, y, text=text, fill="#333333", font="Arial 13 bold", anchor="nw"))

'''
--------------------------------------------------------------------------------------
update
'''
def dev_update(box, command=1):
	if command==1:
		pass
	else:
		pass
'''

--------------------------------------------------------------------------------------
delete
'''
def dev_delete(box):
	pass