from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock

HOST = ''
PORT = 5500
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
HOST_NAME = socket.gethostname()
HOST_IP = socket.gethostbyname(HOST_NAME)

def broadcast(msg):
    pass

def exception_quit():
    pass

def connection_handler(client_socket):
    first_message = 'Welcome to the chat'+'You can type {quit} to exit'+'Now, please type in your name'
    client_socket.send(bytes(first_message,"utf8"))
    name = client_socket.recv(BUFSIZ).decode("utf8")
    sec_message = f"{name} has joined the chat. Welcome!"
    broadcast(sec_message)
    no_error = True
    while no_error:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            if msg != "{quit}":
                broadcast(msg)
            else:
                exception_quit()
        except:
            print("connection_handler: an Error has occured")
            no_error=False




def accept_connections():
    """listen to connections and send them to the client handler"""
    no_error = True
    while no_error:
        try:
            client_socket, client_addr = SERVER.accept()
            print(f"A new client {client_addr} has connected")
            Thread(target=connection_handler, args=(client_socket,)).start()
        except:
            print("accept_connection: A problem has occured")
            no_error = False


if __name__ == "__main__":
    SERVER.listen(5)  # open server to listen for connections
    print("Waiting for connections...")
    ACCEPT_THREAD = Thread(target=accept_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()






