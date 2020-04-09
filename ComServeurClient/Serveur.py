
import	socket
import time

HOST = ''
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
	server.bind((HOST, PORT))
except socket.error:
	print("error")
	exit(1)

print('Serveur en attente')
	
while True:
	server.listen(2)
	connexion, address = server.accept()
	print('nouvelle connexion')

	connexion.send('connexion etablie au serveur '.encode('utf-8'))
	time.sleep(5)
	print('envoie quit')
	connexion.send('QUIT'.encode('utf-8'))
	break
