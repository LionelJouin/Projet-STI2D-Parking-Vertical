import os
import socket

from src.style.funct import *



def is_connected():
	try:
		host = socket.gethostbyname("www.google.com")
		s = socket.create_connection((host, 80), 2)
		if_connectedtointernet(1)
		s.close()
	except:
		if_connectedtointernet(0)

def test_envoie():
	try:
		envoyer('0000')
	except:
		if_connectedtosystem(0)

def se_connecter(ip, port):
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, int(port)))
		#s.connect(("192.168.1.200", 1337))
		s.setblocking(1)

		define_socket(s)
		#print(s)

		code = ""
		place = 15
		accept = 0
		entrantsortant = 2

		if_connectedtosystem(1)
		while is_connectedtosystem()==1:
			try:
				data = s.recv(1024)
				if str(data, 'utf-8')!='0000':
					print("-------------------------------------")
					print("Données recu : ", str(data, 'utf-8'))
					print("-------------------------------------")
				recevoir = str(data, 'utf-8')
				if recevoir[0]=="U":
					code = recevoir[1:]
				elif recevoir[0]=="u":
					accept = int(recevoir[1])
					add_last_places(place, code, entrantsortant, accept)
					if place < 15:
						set_place_dispo(place, entrantsortant, code)
					code = ""
					place = 15
					accept = 0
					entrantsortant = 2
				elif recevoir[0]=="T":
					pass
				elif recevoir[0]=="t":
					pass
				elif recevoir[0]=="S":
					place = int(recevoir[1:])
				elif recevoir[0]=="s":
					entrantsortant = int(recevoir[1])
				elif recevoir[0]=="R":
					if recevoir[1]=="0":
						load_config()
					else:
						pass
			#except:
			except Exception as e:
				print(str(e))
				print("|||||||||||||||||||||||||||||||||||||")
				print("KOUKOU")
				print("|||||||||||||||||||||||||||||||||||||")
				if_connectedtosystem(0)
				break
				
		s.close()

	except:
		print("|||||||||||||||||||||||||||||||||||||")
		print("KOUKOU 2")
		print("|||||||||||||||||||||||||||||||||||||")
		if_connectedtosystem(0)

# U : code rentre                  			U0100B87A09
# u : code valide                  			u1
# T : nombre de place disponnible  			T14
# t : places occupees              			t10000000000000
# S : place de la voiture          			S1
# s : etat (voiture entrante/sortante)      s1