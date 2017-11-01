import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#TODO add server address
client.connect(('0.0.0.0',9999))

client.send('text!')
#TODO change this for other type of buffer
response = client.recv(4096)

print response

