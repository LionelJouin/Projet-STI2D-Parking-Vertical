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



connected = 0


listcode = ['0100b87a09', '0000c2f7ee', '0001f2f00', '1111c3a56', '1010a5c89', '1100b9b96', '1110e6d23', '1001f5e12', '0001f2f35', '1100a3c01', '1111a6c25', '0000b5d21', '0001d9e55', '0100c1f65', '0110d0a36']
listcode_f = ['0010e5b22', '1110f6f99', '0000f5b69', '0101a2c26']



def clientthread(conn, addr):
    global connected


    while connected==1:
        try:
            data = conn.recv(1024)
            if not data:
                if connected==1:
                    connected = 0
                    print(str(addr[0])+":"+str(addr[1])+" s'est deconnecté")
                break
            if str(data, 'utf-8')!='0000':
                print(str(addr[0])+':'+str(addr[1])+' -> '+str(data, 'utf-8'))
        except:
            if connected==1:
                connected = 0
                print(str(addr[0])+":"+str(addr[1])+" s'est deconnecté")
            break
 
def checkclient(conn, addr):
    global connected
    while connected==1:
        time.sleep(5)
        try:
            test = '0000'
            conn.send(test.encode('ascii'))
        except:
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
        print("(1) Envoi configuration")
        print("(2) badge accepté (sortant)")
        print("(3) badge accepté (entrant)")
        print("(4) badge refusé")
        q = int(input())
        if connected==1:
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
                time.sleep(0.05)
                conn.send(place.encode('ascii'))
                time.sleep(0.05)
                conn.send(etates.encode('ascii'))
                time.sleep(0.05)
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
                time.sleep(0.05)
                conn.send(place.encode('ascii'))
                time.sleep(0.05)
                conn.send(etates.encode('ascii'))
                time.sleep(0.05)
                conn.send(etat.encode('ascii'))
                
            if q == 4:
                etat = "u0"
                #code = "U586fd542ac"
                code = "U"+listcode_f[random.randint(0,3)]
                conn.send(code.encode('ascii'))
                time.sleep(0.05)
                conn.send(etat.encode('ascii'))

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