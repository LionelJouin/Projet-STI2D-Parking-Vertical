import socket
import threading
 
print("~ Client Python ~")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("172.18.41.100", 1337))
s.connect(("172.18.41.100", 1337))

# ENVOYER
# Z : Envoyer un nouveau code                       Z0100b87a09
# z : Supprimer un code                             Z0100b87a09
# Y : Activer une place du parking                  Y12
# y : Desactiver une place du parking               y12
# X : Activer le parking                            X
# x : Desactiver le parking                         x
# W : Associer un badge a une place                 W0100b87a0912
# w : Enlever l'association d'un badge a une place  w0100b87a0912
# V : test envoie cote arduino | reception cote 

# RECEVOIR
# U : code rentre                           U0100B87A09
# u : code valide                           u1
# T : nombre de place disponnible           T14
# t : places occupees                       t10000000000000
# S : place de la voiture                   S1
# s : etat (voiture entrante/sortante)      s1
'''
0100b87a09
0000c2f7ee
'''


def serveur():
    while 1:
        try:
            # It will hang here, even if I do close on the socket
            data = s.recv(1024)
            print("-------------------------------------")
            print("Données recu : ", str(data, 'utf-8'))
            print("-------------------------------------")
            # self.clientSocket.send(data)
        except:
            print("|||||||||||||||||||||||||||||||||||||")
            print("KOUKOU")
            print("|||||||||||||||||||||||||||||||||||||")
            break

threading.Thread(target=serveur).start()

q = 0
while q != 3:
 
    print("")
    print("- Menu LAPYTHON -")
    print("(1) ajouter un code")
    print("(2) supprimer un code")
    print("(3) Activer une place de parking")
    print("(4) Desactiver une place du parking")
    print("(5) Activer le parking ")
    print("(6) Desactiver le parking")
    print("(7) Associer un badge a une place")
    print("(8) Enlever l'association d'un badge a une place")
    print("(9) test de reception")
    #q = int(raw_input())
    q = int(input())
     
    if q == 1:
        code = input()
        print("ajout du code : ", code)
        code = 'Z'+code
        s.send(code.encode('ascii'))
        continue
 
    if q == 2:
        code = input()
        print("supprime le code : ", code)
        code = 'Z'+code
        s.send(code.encode('ascii'))

    if q == 3:
        code = input()
        print("Activer la place de parking : ", code)
        code = 'Y'+code
        s.send(code.encode('ascii'))

    if q == 4:
        #s.send('a')
        code = input()
        print("Desactiver la place du parking : ", code)
        code = 'y'+code
        s.send(code.encode('ascii'))

    if q == 5:
        #s.send('a')
        print("Activer le parking")
        code = 'X'
        s.send(code.encode('ascii'))

    if q == 6:
        #s.send('a')
        print("Desactiver le parking")
        code = 'x'
        s.send(code.encode('ascii'))

    if q == 7:
        #s.send('a')
        code = input()
        print("Associer un badge a une place", code)
        code = 'W'+code
        s.send(code.encode('ascii'))

    if q == 8:
        #s.send('a')
        code = input()
        print("Enlever l'association d'un badge a une place ", code)
        code = 'w'+code
        s.send(code.encode('ascii'))

    if q == 9:
        #s.send('a')
        print("test de reception")
        code = 'V'
        s.send(code.encode('utf-8'))
 

print("a+ !")
s.close()
