import os

from tkinter import * 
from src.style.funct import *

class submenu:

	# est executer quand la class est demander
	def __init__(self, window):
		# appele de la classe de recuperation
		self.submenu = Canvas(window, width=192, height=480-64, background='#bdc3c7',borderwidth=0, highlightthickness=0)
		self.submenu.pack(side="left", fill = "both", expand = 0)
		self.rectangle = []
		self.text = []
		self.img = []
		self.image = []
		self.line = []
		self.rect = []
		#self.create_submenu('Visualisation du système', 0)
		#self.create_submenu('Gestion des badges', 1)
		#self.create_submenu('Utilisation du parking', 2)
		self.menu = get_selected_menu()
		self.def_submenu(self.menu)

	def create_submenu(self, text, id):
		calcul = (36+1)*id
		if id == get_selected_submenu():
			self.rectangle.append(self.submenu.create_rectangle(0, 0+calcul, 192, 36+calcul, fill='#afb5b8', width=0))
		else:
			self.rectangle.append(self.submenu.create_rectangle(0, 0+calcul, 192, 36+calcul, fill='#bdc3c7', width=0))
		self.text.append(self.submenu.create_text(10, 18+calcul, text=text, fill="#333333", font="Arial 10 bold", anchor=W))
		self.img.append(PhotoImage(file="data/img/arrow.png"))
		self.image.append(self.submenu.create_image(177, 18+calcul, image=self.img[id]))
		self.line.append(self.submenu.create_line(0,36+calcul,192,36+calcul, fill='#a6abae'))
		self.rect.append(self.submenu.create_rectangle(0, 0+calcul, 192, 36+calcul, width=0))
		self.submenu.tag_bind(self.rect[id], '<Enter>', lambda event, id=id: self.onObjectOver(id)) 
		self.submenu.tag_bind(self.rect[id], '<Leave>', lambda event, id=id: self.onObjectOutOver(id)) 
		self.submenu.tag_bind(self.rect[id], '<ButtonRelease-1>', lambda event, id=id: self.onObjectClick(id))

		
	def del_menu(self):
		self.submenu.unbind_all('<Enter>')
		self.submenu.unbind_all('<Leave>')
		self.submenu.unbind_all('<ButtonRelease-1>')
		self.submenu.delete(ALL)
		self.rectangle = []
		self.text = []
		self.img = []
		self.image = []
		self.line = []
		self.rect = []

	def onObjectClick(self, id):
		self.submenu.itemconfigure(self.rectangle[get_selected_submenu()], fill='#bdc3c7')
		self.submenu.itemconfigure(self.text[get_selected_submenu()])
		self.submenu.itemconfigure(self.rectangle[id], fill='#afb5b8')
		self.submenu.itemconfigure(self.text[id])
		define_selected_submenu(id)

	def onObjectOver(self, id):
		if id != get_selected_submenu():
			self.submenu.itemconfigure(self.rectangle[id], fill='#afb5b8')
			self.submenu.itemconfigure(self.text[id])
		
	def onObjectOutOver(self, id):
		if id != get_selected_submenu():
			self.submenu.itemconfigure(self.rectangle[id], fill='#bdc3c7')
			self.submenu.itemconfigure(self.text[id])

	def detectvarchange(self):
		if self.menu != get_selected_menu():
			self.menu = get_selected_menu()
			self.del_menu()
			define_selected_submenu(0)
			self.def_submenu(self.menu)

	def def_submenu(self, id):
		if id == 0:
			self.create_submenu('Surveillance du parking', 0)
			self.create_submenu('Contrôle du parking', 1)
			self.create_submenu('Gestion des badges', 2)
			self.create_submenu('Utilisation du parking', 3)
		elif id == 1:
			self.create_submenu('Sauvegarde', 0)
			self.create_submenu('Restauration du système', 1)
			self.create_submenu('Paramètres', 2)
		elif id == 2:
			self.create_submenu('Développement', 0)
			self.create_submenu('Système', 1)


