import os

from tkinter import * 

class header:

	# est executer quand la class est demander
	def __init__(self, window):
		# appele de la classe de recuperation
		self.header = Canvas(window, width=600, height=64, background='#292929',borderwidth=0, highlightthickness=0)
		self.header.create_text(84, 20, text='Parking vertical', fill="#ecf0f1", font="Arial 16", anchor=W) 
		self.header.create_text(84, 40, text='STI2D (Python 3.4.2)', fill="#ecf0f1", font="Arial 10", anchor=W) 
		
		self.logo = PhotoImage(file="data/img/logo.png")
		self.header.create_image(7, 32, image=self.logo, anchor=W)
		
		self.header.pack(side="top", fill = "both", expand = 0)
