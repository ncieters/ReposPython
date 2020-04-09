import	socket

import time


HOST = ''

PORT = 8000



connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connexion..')

try:

    print('connexion..')

    connexion.connect((HOST, PORT))

except socket.error:

	print('erre')

	exit(1)



while True:

    msg = connexion.recv(1024).decode('utf-8')

    print('message recu [' + msg +']')

    if msg == "QUIT":

        break

    else:

        print("pas ok")



connexion.close()

print('fin')    