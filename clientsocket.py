import socket

c=socket.socket()
c.connect(("localhost",9998))
while True:
    userinput = input("enter the input : ")
    c.send(bytes(userinput,"utf-8"))

print(c.recv(1024).decode())