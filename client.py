import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
while True:
	value = input()
	clientsocket.send(bytes(value, 'UTF-8'))