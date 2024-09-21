import socket

s = socket.socket()
print("socet created")
s.bind(('localhost',9999))

s.listen(5)
print("Server is listening")

while True:
    c,addr = s.accept()
    print("connected with ",c)
    c.send("msg sent")
    c.close()