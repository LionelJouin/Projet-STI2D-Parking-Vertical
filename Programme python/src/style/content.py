import os

from tkinter import * 
from src.style.funct import *

from src.pages.parkingmonitoring import *
from src.pages.parkingcontrol import *
from src.pages.badgesmanagement import *
from src.pages.parkingusage import *

from src.pages.save import *
from src.pages.restoration import *
from src.pages.settings import *
from src.pages.console import *

from src.pages.development import *
from src.pages.system import *

class content:

	# est executer quand la class est demander
	def __init__(self, window):
		# appele de la classe de recuperation
		self.content = Canvas(window, width=600-320, height=480-128, background='#ecf0f1',borderwidth=0, highlightthickness=0)
		self.content.pack(side="top", fill = "both", expand = 1)
		self.make_content()
		self.menu = get_selected_menu()
		self.submenu = get_selected_submenu()
		self.content.bind('<Configure>', self.varchange_resize)
		
		set_checking_var("pm_p_active", places_active().count(0))
		set_checking_var("pm_p_dispo", places_dispo().count(0))
		
		set_checking_var("bm_nb_badges", get_autorized_badges('size', 1))
		set_checking_var("bm_page_select", 0)
		set_checking_var("bm_page_select_old", 0)
		set_checking_var("bm_notific", "Aucune notification")

		set_checking_var("pu_page_select", 0)
		set_checking_var("pu_page_select_old", 0)

		set_checking_var("seconde", last_places('seconde', 0))

	def varchange_resize(self, event):
		self.make_content(2)

	def detectvarchange(self):
		self.make_content(1)
		if self.menu != get_selected_menu():
			self.content_delete()
			self.menu = get_selected_menu()
			self.make_content()
		if self.submenu != get_selected_submenu():
			self.content_delete()
			self.submenu = get_selected_submenu()
			self.make_content()

	
	def make_content(self, update=0):
		if get_selected_menu() == 0:
			if get_selected_submenu() == 0:   # Surveillance du parking
				if update==0:
					pm_init(self.content)
				else: 
					pm_update(self.content, update)
			elif get_selected_submenu() == 1: # Contrôle du parking
				if update==0:
					pc_init(self.content)
				else:
					pc_update(self.content, update)
			elif get_selected_submenu() == 2: # Gestion des badges
				if update==0:
					bm_init(self.content)
				else:
					bm_update(self.content, update)
			elif get_selected_submenu() == 3: # Utilisation du parking
				if update==0:
					pu_init(self.content)
				else:
					pu_update(self.content, update)
			else: 
				pass
		elif get_selected_menu() == 1:
			if get_selected_submenu() == 0:   # Sauvegarde
				if update==0:
					sav_init(self.content)
				else:
					sav_update(self.content, update)
			elif get_selected_submenu() == 1: # Restauration du système
				if update==0:
					res_init(self.content)
				else:
					res_update(self.content, update)
			elif get_selected_submenu() == 2: # Paramètres
				if update==0:
					set_init(self.content)
				else:
					set_update(self.content, update)
			elif get_selected_submenu() == 3: # Console
				if update==0:
					co_init(self.content)
				else:
					co_update(self.content, update)
			else: 
				pass
		elif get_selected_menu() == 2:
			if get_selected_submenu() == 0:   # Développement
				if update==0:
					dev_init(self.content)
				else:
					dev_update(self.content, update)
			elif get_selected_submenu() == 1: # Système
				if update==0:
					sys_init(self.content)
				else:
					sys_update(self.content, update)
			else: 
				pass
		else:
			pass

	def content_delete(self):
		self.content.delete("all")
		self.content.unbind_all('<Enter>')
		self.content.unbind_all('<Leave>')
		self.content.unbind_all('<ButtonRelease-1>')

		if self.menu == 0:
			if self.submenu == 0:   # Surveillance du parking
				pm_delete(self.content)
			elif self.submenu == 1: # Contrôle du parking
				pc_delete(self.content)
			elif self.submenu == 2: # Gestion des badges
				bm_delete(self.content)
			elif self.submenu == 3: # Utilisation du parking
				pu_delete(self.content)
			else: 
				pass
		elif self.menu == 1:
			if self.submenu == 0:   # Sauvegarde
				sav_delete(self.content)
			elif self.submenu == 1: # Restauration du système
				res_delete(self.content)
			elif self.submenu == 2: # Paramètres
				set_delete(self.content)
			elif self.submenu == 3: # Console
				co_delete(self.content)
			else: 
				pass
		elif self.menu == 2:
			if self.submenu == 0:   # Développement
				dev_delete(self.content)
			elif self.submenu == 1: # Système
				sys_delete(self.content)
			else: 
				pass
		else:
			pass

		'''
		pm_delete(self.content)
		pc_delete(self.content)
		bm_delete(self.content)
		pu_delete(self.content)
		sav_delete(self.content)
		res_delete(self.content)
		set_delete(self.content)
		dev_delete(self.content)
		sys_delete(self.content)
		'''
