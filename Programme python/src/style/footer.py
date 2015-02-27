import os
import threading

from tkinter import * 
from src.style.funct import *
from src.network.funct import *

class footer:

	# est executer quand la class est demander
	def __init__(self, window):
		# appele de la classe de recuperation
		#self.footer = Canvas(window, width=600-128, height=64, background='#292929',borderwidth=0, highlightthickness=0)
		self.footer = Canvas(window, width=600-320, height=64, background='#292929',borderwidth=0, highlightthickness=0)
		self.footer.pack(side="bottom", fill = "both", expand = 0)

		self.connecterausyteme = 0
		self.connecterainternet = 0
		self.threadsystem = ""

		self.ip = StringVar()
		self.ipentry = Entry(self.footer, width=14, bd=0, bg='#292929', fg='#bdc3c7', disabledbackground='#292929', disabledforeground='#bdc3c7', font="Arial 10 bold", textvariable=self.ip)
		self.ipentry.place(x=75, y=5, anchor=NW)
		self.ipentry.insert(0, "172.18.41.8")

		self.port = StringVar()
		self.portentry = Entry(self.footer, width=4, bd=0, bg='#292929', fg='#bdc3c7', disabledbackground='#292929', disabledforeground='#bdc3c7', font="Arial 10 bold", textvariable=self.port)
		self.portentry.place(x=180, y=5, anchor=NW)
		self.portentry.insert(0, "1337")

		self.ipport = Label(self.footer, text="IP:PORT :", bd=0, fg='#bdc3c7', font="Arial 10 bold", background='#292929')
		self.ipport.place(x=5, y=5, anchor=NW)

		self.connecter = Label(self.footer, text="Vous êtes connecté à internet", bd=0, fg='#bdc3c7', font="Arial 10 bold", background='#292929')
		self.connecter.place(x=5, y=64, anchor=SW)

		self.connexionback = ""
		self.connexiontext = ""
		self.connexion = ""
		
		self.connexionback = self.footer.create_rectangle(5, 25, 140, 50, width=0, fill='#3498db')
		self.connexiontext = self.footer.create_text(70, 27, text="Se connecter", fill="#333333", font="Arial 11 bold", anchor=N)
		self.connexion = self.footer.create_rectangle(5, 25, 140, 50, width=0)
		self.footer.tag_bind(self.connexion, '<Enter>', self.onObjectOver) 
		self.footer.tag_bind(self.connexion, '<Leave>', self.onObjectOutOver) 
		self.footer.tag_bind(self.connexion, '<ButtonRelease-1>', self.onObjectClick) 
		
		self.connect_system()
		self.connect_internet()

	def connect_system(self):
		if is_connectedtosystem() == 1:
			self.ipentry.configure(state=DISABLED)
			self.portentry.configure(state=DISABLED)
			self.footer.itemconfigure(self.connexionback, fill='#e74c3c')
			self.footer.itemconfigure(self.connexiontext, text="Se déconnecter")
		else:
			self.ipentry.configure(state=NORMAL)
			self.portentry.configure(state=NORMAL)
			self.footer.itemconfigure(self.connexionback, fill='#3498db')
			self.footer.itemconfigure(self.connexiontext, text="Se connecter")

	def connect_internet(self):
		if is_connectedtointernet() == 0:
			self.connecter.configure(text="Vous n'êtes pas connecté à internet")
		else:
			self.connecter.configure(text="Vous êtes connecté à internet")

	def onObjectClick(self, event):	
		if is_connectedtosystem() == 0:
			#threading.Thread(target=se_connecter).start()
			self.threadsystem = threading.Thread(target=se_connecter, args=(self.ipentry.get(), self.portentry.get(),))
			#self.threadsystem = threading.Thread(target=se_connecter)
			self.threadsystem.start()
		else:
			if_connectedtosystem(0)
	
	def onObjectOver(self, event):
		if is_connectedtosystem() == 1:
			self.footer.itemconfigure(self.connexionback, fill='#c0392b')
		else:
			self.footer.itemconfigure(self.connexionback, fill='#2980b9')
		self.footer.itemconfigure(self.connexiontext)
		
	def onObjectOutOver(self, event):
		if is_connectedtosystem() == 1:
			self.footer.itemconfigure(self.connexionback, fill='#e74c3c')
		else:
			self.footer.itemconfigure(self.connexionback, fill='#3498db')
		self.footer.itemconfigure(self.connexiontext)

	def update(self):
		if self.connecterainternet != is_connectedtointernet():
			self.connect_internet()
			self.connecterainternet = is_connectedtointernet()
		if self.connecterausyteme != is_connectedtosystem():
			self.connect_system()
			self.connecterausyteme = is_connectedtosystem()