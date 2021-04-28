import socket
import sys

HOST = ""
PORT = int(sys.argv[1])
CC = 'utf-8'

print("Create socket...", end="")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(" [DONE] ")

print("Bind socket to port...", end="")
s.bind((HOST,PORT))
print(" [DONE] ")

print("Start listening...", end="")
s.listen()
print(" [DONE] ")

print("Waiting for first connection...")
conn1, addr1 = s.accept()
print (f"First connection from {addr1} [DONE]")
conn1.sendall("Welcome to my chat server!\n".encode(CC))


print("Waiting for second connection...")
conn2, addr2 = s.accept()
print (f"Second connection from {addr2} [DONE]")
conn2.sendall("Welcome to my chat server!\n".encode(CC))




while True:
    print(f"Waiting for message from {addr1}...")
    message = conn1.recv(1024)
    if not message: break
    message = message.decode(CC).rstrip("\r\n")
    conn1.sendall(f"ACK on message: {message}\n".encode(CC))
    conn2.sendall(f"Message from {addr1}: {message}\n".encode(CC))
    print(f"{addr1}: {message}\n")
    if message=="close": break

    print(f"Waiting for message from {addr2}...")
    message = conn2.recv(1024)
    if not message: break
    message = message.decode(CC).rstrip("\r\n")
    conn2.sendall(f"ACK on message: {message}\n".encode(CC))
    conn1.sendall(f"Message from {addr1}: {message}\n".encode(CC))
    print(f"{addr2}: {message}\n")
    if message=="close": break




conn1.close()
conn2.close()
s.close()




