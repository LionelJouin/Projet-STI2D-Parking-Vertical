import os
import time
import threading
import sys

from tkinter import * 
from src.style.funct import *
from src.style.header import *
from src.style.menu import *
from src.style.submenu import *
from src.style.content import *
from src.style.footer import *
from src.style.footer import *

# class principal du menu
class main:

	# est executer quand la class est demander
	def __init__(self):
		# Initialisation de la bibliotheque TKinter
		window = Tk()
		# Nom de la fenetre
		window.title('STI2D - Parking vertical')
		# couleur de fond
		window['bg'] = '#ecf0f1'
		# icone de la fenetre
		window.iconbitmap("data/img/logo.ico")
		# definie la taille et les bords de la fenetre
		define_sizescreen( ( window.winfo_screenwidth() , window.winfo_screenheight() ) )
		define_sizenpos( ( pxltopercent(infos("largeur_fenetre_percent"),infos("largeur_ecran")) , pxltopercent(infos("hauteur_fenetre_percent"),infos("hauteur_ecran")) ) , (0,0) )
		define_sizenpos( ( infos("largeur_fenetre") , infos("hauteur_fenetre") ) , ( int((infos("largeur_ecran")-infos("largeur_fenetre"))/2) , int((infos("hauteur_ecran")-infos("hauteur_fenetre"))/2) ) )

		# taille de la fenetre
		window.geometry("600x480+"+ str(infos("position_x")) +"+"+ str(infos("position_y")) )
		window.minsize(600, 480)

		# chargement de la base de données
		load_database()

		# appel de l'entete
		self.header = header(window)
		# appel du menu
		self.menu = menu(window)
		# appel du sous-menu
		self.submenu = submenu(window)
		# appel du contenu
		self.content = content(window)
		# appel du pied 
		self.footer = footer(window)
		
		# detect changement de menu
		#window.bind('<ButtonRelease-1>', self.detectvarchange)
		#window.bind('<Configure>', self.varchange_resize)
		threading.Thread(target=self.varchange).start()
		threading.Thread(target=self.varchange_slow).start()

		# taille de la fenetre
		window.geometry( str(infos("largeur_fenetre")) +"x"+ str(infos("hauteur_fenetre")) +"+"+ str(infos("position_x")) +"+"+ str(infos("position_y")) )

		# variable de chargement de l'application
		set_checking_var('chargement', 1)

		self.konami = 0
		window.bind('<Key>', self.konamicode)

		# boucle principal
		window.mainloop()

	def detectvarchange(self, event):
		self.submenu.detectvarchange()
		self.content.detectvarchange()
		print("Menu : "+str(get_selected_menu()))
		print("Sous-menu : "+str(get_selected_submenu()))

	def varchange(self):
		while 1==1:
			time.sleep(0.1)
			#time.sleep(0.1)
			self.submenu.detectvarchange()
			self.content.detectvarchange()
			self.footer.update()

	def varchange_slow(self):
		while 1==1:
			is_connected()
			test_envoie()
			time.sleep(5)

	def varchange_resize(self, event):
		print("x : "+str(event.width))
		print("y : "+str(event.height))

	def konamicode(self, event):
		if str(event.keysym)=="Up" and self.konami==0:
			self.konami = 1
		elif  str(event.keysym)=="Up" and self.konami==1:
			self.konami = 2
		elif  str(event.keysym)=="Down" and self.konami==2:
			self.konami = 3
		elif  str(event.keysym)=="Down" and self.konami==3:
			self.konami = 4
		elif  str(event.keysym)=="Left" and self.konami==4:
			self.konami = 5
		elif  str(event.keysym)=="Right" and self.konami==5:
			self.konami = 6
		elif  str(event.keysym)=="Left" and self.konami==6:
			self.konami = 7
		elif  str(event.keysym)=="Right" and self.konami==7:
			self.konami = 8
		elif  str(event.keysym)=="b" and self.konami==8:
			self.konami = 9
		elif  str(event.keysym)=="a" and self.konami==9:
			print("konami code")
		else:
			self.konami = 0
