from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

# GLOBAL VARIABLES
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 1024
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def client_communication(person):
    """
    Thread to handle all messages from clients
    :param client: socket
    :return:
    """
    run = True
    while run:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            client.close()
        else:


def wait_for_connection(SERVER):
    """
    Wait for connection from new client, start new thread
    :param SERVER: socket
    :return: None
    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(client,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False




if __name__ == '__main__':
    SERVER.listen(MAX_CONNECTIONS)    # listen for connections
    print("Waiting for a connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()