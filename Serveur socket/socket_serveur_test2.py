'''
    Simple socket server using threads
'''
 
import socket
import sys
import threading
import time
import random
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 1337 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
print(socket.gethostbyname(socket.gethostname()))
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print(msg)
	#print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(5)
print('Socket now listening')
 
#Function for handling connections. This will be used to create threads
def clientthread(conn, addr):
	#Sending message to connected client
	#conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
	msg = "koukou"
	conn.send(msg.encode('ascii'))
     
	#infinite loop so that function do not terminate and thread do not end.
	while True:
		#Receiving from client
		data = conn.recv(1024)
		reply = '0000'
		if not data: 
			break
		#print(data)
		print(str(addr[0])+':'+str(addr[1])+' -> '+str(data, 'utf-8'))
		#conn.sendall(reply.encode('ascii'))
		
	#came out of loop
	conn.close()
 
def checkclient(conn, addr):
	while True:
		time.sleep(5)
		try:
			test = '0000'
			conn.send(test.encode('ascii'))
		except:
			print(str(addr[0])+":"+str(addr[1])+" s'est deconnecté")
	
#now keep talking with the client
while 1:
	#wait to accept a connection - blocking call
	conn, addr = s.accept()
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	#start_new_thread(clientthread ,(conn,))
	threadclient = threading.Thread(target=clientthread, args=(conn, addr))
	threadclient.start()
	threadcheck = threading.Thread(target=checkclient, args=(conn, addr))
	threadcheck.start()
 
s.close()