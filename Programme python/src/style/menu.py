import os

from tkinter import * 
from src.style.funct import *

class menu:

	# est executer quand la class est demander
	def __init__(self, window):
		# appele de la classe de recuperation
		self.menu = Canvas(window, width=128, height=480-64, background='#333333',borderwidth=0, highlightthickness=0)
		self.menu.pack(side="left", fill = "both", expand = 0)
		self.rectangle = []
		self.text = []
		self.img = []
		self.image = []
		self.line = []
		self.rect = []
		self.create_menu('Parking \nVertical', "data/img/parking.png", 0)
		self.create_menu('Outils', "data/img/tools.png", 1)
		self.create_menu('Á propos', "data/img/apropos.png", 2)

	def create_menu(self, text, img, id):
		calcul = (128+1)*id
		if id == get_selected_menu():
			self.rectangle.append(self.menu.create_rectangle(0, 0+calcul, 128, 128+calcul, fill='#2ecc71',width=0))
		else:
			self.rectangle.append(self.menu.create_rectangle(0, 0+calcul, 128, 128+calcul, fill='#333333',width=0))
		self.text.append(self.menu.create_text(64, 102+calcul, text=text, fill="#ecf0f1", font="Arial 13 bold"))
		self.img.append(PhotoImage(file=img))
		self.image.append(self.menu.create_image(64, 45+calcul, image=self.img[id]))
		self.line.append(self.menu.create_line(0,128+calcul,128,128+calcul, fill='black'))
		self.rect.append(self.menu.create_rectangle(0, 0+calcul, 128, 128+calcul, width=0))
		self.menu.tag_bind(self.rect[id], '<Enter>', lambda event, id=id: self.onObjectOver(id)) 
		self.menu.tag_bind(self.rect[id], '<Leave>', lambda event, id=id: self.onObjectOutOver(id)) 
		self.menu.tag_bind(self.rect[id], '<ButtonRelease-1>', lambda event, id=id: self.onObjectClick(id))
		
	def onObjectClick(self, id):
		self.menu.itemconfigure(self.rectangle[get_selected_menu()], fill='#333333')
		self.menu.itemconfigure(self.text[get_selected_menu()])
		self.menu.itemconfigure(self.rectangle[id], fill='#2ecc71')
		self.menu.itemconfigure(self.text[id])
		define_selected_menu(id)

	def onObjectOver(self, id):
		if id != get_selected_menu():
			self.menu.itemconfigure(self.rectangle[id], fill='#1C1C1C')
			self.menu.itemconfigure(self.text[id])
		
	def onObjectOutOver(self, id):
		if id != get_selected_menu():
			self.menu.itemconfigure(self.rectangle[id], fill='#333333')
			self.menu.itemconfigure(self.text[id])

