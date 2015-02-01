#!/usr/bin/env python
# coding=utf-8

if __name__ == "__main__":
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time
    time.sleep(2)
    while True:
        sock.send("Request Send Info")
        print (sock.recv(1024))
    sock.close()
