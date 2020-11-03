import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))

while True:
    content = bytes(input('Please input you want speak: '),encoding='utf-8')
    #cb = bytes(content,encoding='utf-8')
    if content == b'exit':
        print("hehehe")
        break
    s.send(content)
    print(s.recv(1024).decode('utf-8'))
