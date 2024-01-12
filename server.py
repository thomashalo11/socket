import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# Creazione della socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di messaggi... ")

while True:
    # Ricezione dei dati del clinet
    data, addr = sock.recfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal client {addr}: {data.decode()}")

    # Invio di una risposta al clinet
    reply = "pong"
    sock.sendto(reply.encode(), addr)