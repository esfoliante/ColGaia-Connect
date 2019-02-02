#This is a The Open-Source Dudes and Wolf Code creation, by: Miguel Ferreira

#!/usr/bin/env python

import socket #this will help us to chat :D

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def error(type): #oohhh did something happened?
	if type == "1": #typing error
		print('Oooops, you type the wrong command, please try again...')
		choice = str(input('Want to create a server (c) or join one (j)? » ')).lower()
		if choice == "c":
			host()
		elif choice == "j":
			join()
		else:
			print('Oooops, you type the wrong command, please try again...')
			while choice != "c" or choice != "j":
				choice = str(input('Want to create a server (c) or join one (j)? » ')).lower()

				if choice == "c":
					host()
					break
				elif choice == "j":
					join()
					break
				else:
					print('Oooops, you type the wrong command, please try again...')
	if error == "2": #connection error
		print('Ohhh, it looks like your frien\'s IP doesn\'t exist')
		print('Close try closing the program :[')
		conn.close()

def host():
	port = 8080 #this will be the default port for all connections (8080 is fancy number isn't it?)
	host = socket.gethostbyname(socket.gethostname()) #what a confusion *-*, basically we'll get the user IP (gethostbyname()) via the OS' name (gethostname())

	print('Hey? You\'re ready to recieve a connection in this IP: {}'.format(host))

	conn.bind((host,port)) #the computer will do some magic and create a connection
	conn.listen(1) #waint for 1 user to connect (don't try this if you have no friends...)
	print('Waiting for a friend to join..........')
	c, friend = conn.accept()

	friend = str(input('Name your friend: '))
	if not friend.strip(): #let's check if friend's name is equals to nothing or a bunch of spaces hehe
		friend = "Friend"

	print('Connected')
	while True:
		message = c.recv(1024)
		print('{}: {}'.format(friend,message.decode()))
		text = str(input('» ')).encode() #user will type his message and the computer will understand it at the sam time (what a curious computer)
		c.send(text)
	c.close() #we need to end the connection :[, mabe the teacher found us

def join():
	port = 8080
	host = str(input('Friend\'s IP: '))

	try:
		conn.connect((host, port))
	except:
		error(type="2")

	friend = str(input('Name your friend: '))
	if not friend.strip(): #let's check if friend's name is equals to nothing or a bunch of spaces hehe
		friend = "Friend"

	print('Connected to {}. Have fun!'.format(friend))

	while True:
		message = str(input('» '))
		message = message.encode() #just read line 55
		conn.send(message)
		data = conn.recv(1024)
		print('{}: {}'.format(friend, data.decode()))
	conn.close() #end connection, but now for the join section :D

print('Welcome to ColGaia-Connect!')
choice = str(input('Want to create a server (c) or join one (j)? » ')).lower()

if choice == "c":
	host()
elif choice == "j":
	join()
else:
	error(type="1")