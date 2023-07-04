import socket
import logging
from threading import Thread, Event

def handle_connection(connection, client_address, four_character_analyzer, stop):
        try:
            logging.info(f'connection from {str(client_address)}')
            # Receive the data in small chunks and retransmit it
            while not stop.is_set():
                data = connection.recv(1024)
                if not data:
                    logging.info("Leaving connection")
                    break
                logging.info('received {!r}'.format(data))
                four_character_analyzer.run(data.decode())
        finally:
            # Clean up the connection
            logging.info("Closing connection")
            connection.close()


MAX_CLIENTS = 5

def run_server(host: str, port: int, stop: Event, four_character_analyzer):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = (host, port)
    logging.info('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(MAX_CLIENTS)
    while not stop.is_set():
        # Wait for a connection
        logging.info('waiting for a connection')
        connection, client_address = sock.accept()
        thread = Thread(target=handle_connection, args=(connection,client_address, four_character_analyzer, stop,  ))
        thread.start()


def run_client(host: str, port: int, message: str):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = (host, port)
    logging.info('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try:
        # Send data
        logging.info('sending {!r}'.format(message))
        sock.sendall(message.encode())
    finally:
        logging.info('closing socket')
        sock.close()

