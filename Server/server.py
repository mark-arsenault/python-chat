from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZE =512

# GLOBAL VARIABLES
persons = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)   # set up server


def broadcast(msg, name):
    """
    send new message to all clients
    :param msg: bytes["utf8"]
    :param name: str
    :return: None
    """
    for person in persons:
        client = person.client
        try:
            client.send(bytes(name, "utf8") + msg)
        except Exception as e:
            print("[EXCEPTION]", e)


def client_communication(person):
    """
    Thread to handle all messages from client
    :param person: Person
    :return: None
    """
    client = person.client

    # first message received will always be name
    name = client.recv(BUFSIZE).decode("utf8")
    person.set_name(name)

    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, "")  # broadcast welcome message

    while True:
        msg = client.recv(BUFSIZE)

        if msg == bytes("{quit}", "utf8"):
            client.close()
            persons.remove(person)
            broadcast(f"{name} has left the chat...", "")
            print(f"[DISCONNECTED] {name} disconnected")
            break
        else:
            client.send(msg, name+": ")
            print(f"{name}: ", msg.decode("utf8"))


def wait_for_connection():
    """
    Wait for connection from new client, start new thread
    :return: None
    """
    while True:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)

            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            break

    print("SERVER CRASHED")


if __name__ == '__main__':
    SERVER.listen(MAX_CONNECTIONS)    # listen for connections
    print("[STARTED] Waiting for a connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()