# http://apprendre-python.com/page-reseaux-sockets-python-port

import socket
import threading
import time
import random
 
print("~ Serveur Python ~")
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("172.18.48.100", 1337))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1337)) # demarrage du serveur
s.listen(5) # nombre maximum de client

# ENVOYER
# Z : Envoyer un nouveau code                       Z0100b87a09
# z : Supprimer un code                             z0100b87a09
# Y : Activer une place du parking                  Y12
# y : Desactiver une place du parking               y12
# X : Activer le parking                            X
# x : Desactiver le parking                         x
# W : Associer un badge a une place                 W0100b87a0912
# w : Enlever l'association d'un badge a une place  w0100b87a0912
# V : test envoie cote arduino | reception cote 

# RECEVOIR
# U : code rentre                  			U0100B87A09
# u : code valide                  			u1
# T : nombre de place disponnible  			T14
# t : places occupees              			t10000000000000
# S : place de la voiture          			S1
# s : etat (voiture entrante/sortante)      s1
'''
0100b87a09
0000c2f7ee

0001f2f00
1111c3a56
1010a5c89
1100b9b96
1110e6d23
1001f5e12
0001f2f35
1100a3c01
1111a6c25
0000b5d21
0001d9e55
0100c1f65
0110d0a36

0010e5b22
1110f6f99
0000f5b69
0101a2c26
'''
listcode = ['0100b87a09', '0000c2f7ee', '0001f2f00', '1111c3a56', '1010a5c89', '1100b9b96', '1110e6d23', '1001f5e12', '0001f2f35', '1100a3c01', '1111a6c25', '0000b5d21', '0001d9e55', '0100c1f65', '0110d0a36']
listcode_f = ['0010e5b22', '1110f6f99', '0000f5b69', '0101a2c26']

(conn, addr) = s.accept()
print(addr[0]+':'+str(addr[1])+' vient de se connecté')

print(addr)
	
def serveur():
    while 1:
        try:
            # It will hang here, even if I do close on the socket
            data = conn.recv(1024)
            if str(data, 'utf-8')=='0000':
                pass
            else:
                print("-------------------------------------")
                print("Données recu : ", str(data, 'utf-8'))
                print("-------------------------------------")
            # self.clientSocket.send(data)
        except:
            print("|||||||||||||||||||||||||||||||||||||")
            print("KOUKOU")
            print("|||||||||||||||||||||||||||||||||||||")
            break

threadserveur = threading.Thread(target=serveur).start()

while True:
    print("")
    print("- Menu LARDUINO -")
    print("(1) Envoi configuration")
    print("(2) badge accepté (sortant)")
    print("(3) badge accepté (entrant)")
    print("(4) badge refusé")
    q = int(input())
    a = 0
    if q == 1:
        code = "code 1"
        conn.send(code.encode('ascii'))

    if q == 2:
        etat = "u1"
        #code = "U0000c2f7ee"
        #place = "S2"
        a = int(input())
        code = "U"+listcode[a]
        place = "S"+str(a)
        etates = "s1"
        conn.send(code.encode('ascii'))
        time.sleep(0.2)
        conn.send(place.encode('ascii'))
        time.sleep(0.2)
        conn.send(etates.encode('ascii'))
        time.sleep(0.2)
        conn.send(etat.encode('ascii'))

    if q == 3:
        etat = "u1"
        #code = "U0000c2f7ee"
        place = "S2"
        a = int(input())
        code = "U"+listcode[a]
        place = "S"+str(a)
        etates = "s0"
        conn.send(code.encode('ascii'))
        time.sleep(0.2)
        conn.send(place.encode('ascii'))
        time.sleep(0.2)
        conn.send(etates.encode('ascii'))
        time.sleep(0.2)
        conn.send(etat.encode('ascii'))
		
    if q == 4:
        etat = "u0"
        #code = "U586fd542ac"
        code = "U"+listcode_f[random.randint(0,3)]
        conn.send(code.encode('ascii'))
        time.sleep(0.2)
        conn.send(etat.encode('ascii'))

