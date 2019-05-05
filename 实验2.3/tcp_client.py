#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


def main():
    host = '127.0.0.1'
    port = 9999
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print('[info] connect to [%s:%d]' % (host, port))

    while True:
        command = input('['+host+':'+str(port)+']$ ')
        client_socket.send(command.encode('utf-8'))
        message = client_socket.recv(2048).decode('utf-8')
        print(message)


if __name__ == '__main__':
    main()
