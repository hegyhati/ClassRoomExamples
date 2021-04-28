import socket
import sys
import threading

HOST = ""
PORT = int(sys.argv[1])
CC = 'utf-8'

clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

def broadcast_message(sender: str, message: str):
    print(f"{sender} broadcasts message: '{message}'")
    for client_name in clients:
        if client_name != sender:
            clients[client_name].sendall(
                f"{sender} >>> {message}\n".encode(CC))

def initialize_connection(conn, addr):
    conn.sendall(
        "[[SYSTEM]] Welcome to my chat server!\nWhat should we call you?\n".encode(CC))
    name = conn.recv(1024).decode(CC).rstrip("\r\n")
    conn.sendall(
        f"[[SYSTEM]] Hello {name}! Others in chat: { list(clients.keys()) }\n".encode(CC))
    broadcast_message("[[SYSTEM]]", f"{name} has joined the chat")
    clients[name] = conn
    message_handler(name)

def message_handler(name):
    while True:
        message = clients[name].recv(1024)
        if not message:
            break
        message = message.decode(CC).rstrip("\r\n")
        clients[name].sendall(b"[ACK]\n")
        broadcast_message(name, message)
        if message == "close":
            clients[name].close()
            break
    del clients[name]
    broadcast_message("[[SYSTEM]]", f"{name} has left the chat.")

while len(clients) < 5:
    conn, addr = s.accept()
    threading.Thread(target=initialize_connection, args=(conn, addr)).start()


for (conn, addr) in clients:
    print(f"Closing connection to {addr}")
    conn.close()
s.close()
