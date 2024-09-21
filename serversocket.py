import socket

s = socket.socket()
print("socet created")
s.bind(('localhost',9998))

s.listen(5)
print("Server is listening")

while True:
    c,addr = s.accept()
    while True:
        userdata = c.recv(1024).decode()
        print(userdata)
    
    c.send(bytes("msg sent","utf-8"))
    c.close()
    