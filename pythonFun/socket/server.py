#!/usr/bin/env python
# coding=utf-8

if __name__ == "__main__":
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)
    connection,address = sock.accept()
    while True:
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            print (buf)
            if buf != None:
                connection.send('welcome to server!')
            else:
                connection.send('please to out')
        except socket.timeout:
            print ("time out")
            connection.close()
