import socket
import sys
import threading
import time
import random
 
print("■■■■■■■■■■■■■■■■■■■■")
print("~ Serveur Python ~")
print("~~~~~~~~~~~~~~~~~~~~")
print("■■■■■■■■■■■■■■■■■■■■")
print("")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print( ' - > Hebergé sur : '+socket.gethostbyname(socket.gethostname())+':1337' )

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
# V : Place prise                                   V0100b87a0912
# v : decharger la place                            v12
# v : redemarrer le systeme                         r

# RECEVOIR
# U : code rentre                                   U0100B87A09
# u : code valide                                   u1
# T : nombre de place disponnible                   T14
# t : places occupees                               t10000000000000
# S : place de la voiture                           S1
# s : etat (voiture entrante/sortante)              s1
# R : configuration coté arduino est charger        R1

connected = 0
parking_actif = 0
config_loaded = 0

listcode = ['0100b87a09', '0000c2f7ee', '00001f2f00', '11110c3a56', '10100a5c89', '11000b9b96', '11100e6d23', '10010f5e12', '00001f2f35', '1100a03c01', '11110a6c25', '00000b5d21', '00001d9e55', '01000c1f65', '01010d0a36']
listcode_f = ['00010e5b22', '11100f6f99', '00000f5b69', '01001a2c26']

code_accept = []
place_active = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
place_dispo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
place_predef = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
place_codes = ['','','','','','','','','','','','','','','']


def clientthread(conn, addr):
    global connected

    if config_loaded==0: # config pas charger
        load = 'R0'
        conn.send(load.encode('ascii'))
    else:
        load = 'R1'
        conn.send(load.encode('ascii'))

    while connected==1:
        
        try:
            data = conn.recv(1024)
            datarecv = str(data, 'utf-8')
            if not data:
                print("1")
                #if connected==1:
                #    connected = 0
                #    print(str(addr[0])+":"+str(addr[1])+" s'est deconnecté")
                break
            if datarecv!='0000':
                print(str(addr[0])+':'+str(addr[1])+' -> '+datarecv)
            if datarecv[0] == 'Z': # Ajoute un code
                code_accept.append(datarecv[1:])
            elif datarecv[0] == 'z': # Supprimer un code
                code_accept.remove(datarecv[1:])
            elif datarecv[0] == 'Y': # Activer une place du parking
                if len(datarecv)==3:
                    place_active[int(datarecv[1:])] = 1
                else:
                    place_active[int(datarecv[1])] = 1
            elif datarecv[0] == 'y': # Desactiver une place du parking
                if len(datarecv)==3:
                    place_active[int(datarecv[1:])] = 0
                else:
                    place_active[int(datarecv[1])] = 0
            elif datarecv[0] == 'X': # Activer le parking
                parking_actif = 1
            elif datarecv[0] == 'x': # Desactiver le parking
                parking_actif = 0
            elif datarecv[0] == 'W': # Associer un badge a une place 
                if len(datarecv)==13:
                    place_predef[int(datarecv[11:12])] = 1
                    place_codes[int(datarecv[11:12])] = datarecv[1:10]
                else:
                    place_predef[int(datarecv[11])] = 1
                    place_codes[int(datarecv[11])] = datarecv[1:10]
            elif datarecv[0] == 'w': # Enlever l'association d'un badge a une place
                if len(datarecv)==13:
                    place_predef[int(datarecv[11:12])] = 0
                    place_codes[int(datarecv[11:12])] = ""
                else:
                    place_predef[int(datarecv[11])] = 0
                    place_codes[int(datarecv[11])] = ""
            elif datarecv[0] == 'V': # Place prise
                if len(datarecv)==13:
                    place_dispo[int(datarecv[11:12])] = 0
                    place_codes[int(datarecv[11:12])] = ""
                else:
                    place_dispo[int(datarecv[11])] = 0
                    place_codes[int(datarecv[11])] = ""
        except:
            print("2")
            if connected==1:
                connected = 0
                print(str(addr[0])+":"+str(addr[1])+" s'est deconnecté")
            break

        '''
        data = conn.recv(1024)
        datarecv = str(data, 'utf-8')
        if not data:
            print("1")
            #if connected==1:
            #    connected = 0
            #    print(str(addr[0])+":"+str(addr[1])+" s'est deconnecté")
            break
        if datarecv!='0000':
            print(str(addr[0])+':'+str(addr[1])+' -> '+datarecv)
        if datarecv[0] == 'Z': # Ajoute un code
            code_accept.append(int(datarecv[1:]))
        elif datarecv[0] == 'z': # Supprimer un code
            code_accept.remove(int(datarecv[1:]))
        elif datarecv[0] == 'Y': # Activer une place du parking
            if len(datarecv)==3:
                place_active[int(datarecv[1:])] = 1
            else:
                place_active[int(datarecv[1])] = 1
        elif datarecv[0] == 'y': # Desactiver une place du parking
            if len(datarecv)==3:
                place_active[int(datarecv[1:])] = 0
            else:
                place_active[int(datarecv[1])] = 0
        elif datarecv[0] == 'X': # Activer le parking
            parking_actif = 1
        elif datarecv[0] == 'x': # Desactiver le parking
            parking_actif = 0
        elif datarecv[0] == 'W': # Associer un badge a une place 
            if len(datarecv)==13:
                place_predef[int(datarecv[11:12])] = 1
                place_codes[int(datarecv[11:12])] = datarecv[1:10]
            else:
                place_predef[int(datarecv[11])] = 1
                place_codes[int(datarecv[11])] = datarecv[1:10]
        elif datarecv[0] == 'w': # Enlever l'association d'un badge a une place
            if len(datarecv)==13:
                place_predef[int(datarecv[11:12])] = 0
                place_codes[int(datarecv[11:12])] = ""
            else:
                place_predef[int(datarecv[11])] = 0
                place_codes[int(datarecv[11])] = ""
        elif datarecv[0] == 'V': # Place prise
            if len(datarecv)==13:
                place_dispo[int(datarecv[11:12])] = 0
                place_codes[int(datarecv[11:12])] = ""
            else:
                place_dispo[int(datarecv[11])] = 0
                place_codes[int(datarecv[11])] = ""
        '''

def checkclient(conn, addr):
    global connected
    while connected==1:
        time.sleep(5)
        try:
            test = '0000'
            conn.send(test.encode('ascii'))
        except:
            print("3")
            if connected==1:
                connected = 0
                print(str(addr[0])+":"+str(addr[1])+" s'est deconnecté")
            break
    conn.close()
    




def menu(conn, addr):
    global connected
    while connected==1:
        print("")
        print("- Menu LARDUINO -")
        print("(1) Voir configuration total")
        print("(2) Voir configuration place")
        print("(3) badge accepté (sortant)")
        print("(4) badge accepté (entrant)")
        print("(5) badge refusé")
        print("(6) place")
        q = ""
        while q=="":
            q = int(input())
        if connected==1:
            a = 0
            if q == 1:
                #code = "code 1"
                #conn.send(code.encode('ascii'))
                #code_accept = []
                #place_active = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                #place_dispo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                #place_predef = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                #place_codes = ['','','','','','','','','','','','','','','']
                print('CODES ACCEPTEES :')
                print('')
                print(code_accept)
                print('')
                print('')
                print('PLACES ACTIVES :')
                print('')
                print(place_active)
                print('')
                print('')
                print('PLACES DISPO :')
                print('')
                print(place_dispo)
                print('')
                print('')
                print('PLACES PREDEFINIES :')
                print('')
                print(place_predef)
                print('')
                print('')
                print('CODES ET PLACES :')
                print('')
                print(place_codes)
                print('')
                print('')

            if q == 2:
                a = ""
                while a=="":
                    a = int(input())
                print('PLACES ACTIVES : '+str(place_active[a]))
                print('PLACES DISPO : '+str(place_dispo[a]))
                print('PLACES PREDEFINIES : '+str(place_predef[a]))
                print('CODES ET PLACES : '+str(place_codes[a]))

            if q == 3:
                etat = "u1"
                #code = "U0000c2f7ee"
                #place = "S2"
                a = ""
                while a=="":
                    a = int(input())
                code = "U"+listcode[a]
                place = "S"+str(a)
                etates = "s1"
                conn.send(code.encode('ascii'))
                time.sleep(0.05)
                conn.send(place.encode('ascii'))
                time.sleep(0.05)
                conn.send(etates.encode('ascii'))
                time.sleep(0.05)
                conn.send(etat.encode('ascii'))

            if q == 4:
                etat = "u1"
                #code = "U0000c2f7ee"
                place = "S2"
                a = ""
                while a=="":
                    a = int(input())
                code = "U"+listcode[a]
                place = "S"+str(a)
                etates = "s0"
                conn.send(code.encode('ascii'))
                time.sleep(0.05)
                conn.send(place.encode('ascii'))
                time.sleep(0.05)
                conn.send(etates.encode('ascii'))
                time.sleep(0.05)
                conn.send(etat.encode('ascii'))
                
            if q == 5:
                etat = "u0"
                #code = "U586fd542ac"
                code = "U"+listcode_f[random.randint(0,3)]
                conn.send(code.encode('ascii'))
                time.sleep(0.05)
                conn.send(etat.encode('ascii'))

            if q == 6:
                place = ""
                code = ""
                etat = ""
                etates = ""

                a = ""
                while a=="":
                    a = int(input())

                if place_predef[a]==1: # si la place est predefinie

                    if place_dispo[a]==1: # si la place est libre
                        place_dispo[a] = 0
                        code = "U"+place_codes[a]
                        etat = "u1"
                        places = "S"+str(a)
                        etates = "s0"
                    else:
                        place_dispo[a] = 1
                        code = "U"+place_codes[a]
                        etat = "u1"
                        places = "S"+str(a)
                        etates = "s1"

                elif place_active[a]==1: # si la place n'est pas predefinie

                    if place_dispo[a]==1: # si la place est libre
                        place_dispo[a] = 0
                        etat = "u1"
                        code = code_accept[random.randint(0,len(code_accept))]
                        places = "S"+str(a)
                        etates = "s0"

                        place_codes[a] = code
                    else:
                        place_dispo[a] = 1
                        code = "U"+place_codes[a]
                        etat = "u1"
                        place_codes[a] = ""
                        places = "S"+str(a)
                        etates = "s1"

                else:
                    'la place est desactiver'


'''               
code_accept = []
place_active = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
place_dispo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
place_predef = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
place_codes = ['','','','','','','','','','','','','','','']
'''



while True:
    print("---------------------------------")
    print("---En attente d'une connection---")
    print("---------------------------------")
    conn, addr = s.accept() # accepte les clients
    connected = 1
    print(addr[0]+':'+str(addr[1])+' vient de se connecté')
    threadclient = threading.Thread(target=clientthread, args=(conn, addr))
    threadclient.start()
    threadcheck = threading.Thread(target=checkclient, args=(conn, addr))
    threadcheck.start()
    menu(conn, addr)


'''
while True:
    print("")
    print("- Menu LARDUINO -")
    print("(1) Envoi configuration")
    print("(2) badge accepté (sortant)")
    print("(3) badge accepté (entrant)")
    print("(4) badge refusé")
    q = int(input())
    test = 'tghrtjiyjrtuiy'
    testz.send(test.encode('ascii'))
'''

s.close()