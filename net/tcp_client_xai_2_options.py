import socket

CRLF = "\r\n\r\n"

HOST = 'google.com'
PORT = 80
SERVER_ADDRESS = (HOST, PORT)

HOST_HTTP_PARAM="google.com"
USER_AGENT_HTTP_PARAM="el.vostre.correu@uoc.edu"

OPTIONS_COMMAND="OPTIONS * HTTP/1.1\nUser-agent: "+USER_AGENT_HTTP_PARAM+"\nHost: "+HOST_HTTP_PARAM+CRLF
def send_options(client):
    client.send(OPTIONS_COMMAND)
    

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#TODO add server address
client.connect(SERVER_ADDRESS)

send_options(client)
#TODO change this for other type of buffer
response = client.recv(4096)

print response
