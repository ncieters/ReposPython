import	socket

HOST = '192.168.139.1'
PORT = 8000

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	connexion.connect((Host, PORT))
except socket.error:
	printf("erre")
	exit(1)

