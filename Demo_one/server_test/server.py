import socket
import threading
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print("Waiting for connection.....")


def tcplink(sock, addr):
    print("Accept new connection from %s:%s..." %addr)

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        elif data.decode('utf-8') == 'PlayGame':
            sock.send(("玩皮呀玩，不准玩").encode('utf-8'))
        else:
            sock.send(('Hello %s 欢迎使用最屌人工助理,Small' % data.decode('utf-8')).encode('utf-8'))
        # sock.send(("Hello %s!" % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("Connection from %s:%s closed." %addr)
    #decode('utf-8') 是使用utf-8来解析
    #encode('utf-8') 是使用utf-8来编码


while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
