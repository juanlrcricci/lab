#!/usr/bin/python3

import socket
import sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print(s)

# get local machine name
host = socket.gethostname()                     
# host = sys.argv[1]

port = 2222 # int(sys.argv[2])

print("Haciendo el connect")
# connection to hostname on the port.
s.connect((host, port))   
print("Handshake realizado con exito!")

comandos = ['nombre', 'email', 'key', 'exit']

for comando in comandos:
    command = input(str("Ingrese su %s: " %comando))
    if comando == 'nombre':
        command = 'hello|' + command
    elif comando == 'email':
        command = 'email|' + command
    elif comando == 'key':
        command = 'key|' + command
    elif comando == 'exit':
        command == comando

    print("Enviando datos al server")
    msg = s.send(command.encode('utf-8'))
    print("Reciviendo datos del server")
    recv = s.recv(1024)
    print(recv.decode())
    

#print (msg.decode('ascii'))
#print (msg.decode('utf-8'))
s.close()
print("Cerrando conexion")
