#Shitty example code I just stole from google.
import socket

HOST = '127.0.0.1'  
PORT = 6210      

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("running on {}:{}".format(HOST, PORT))

socket_client.bind((HOST, PORT))
socket_client.listen()

conn, addr = socket_client.accept()

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)