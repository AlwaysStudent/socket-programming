#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


if __name__ == '__main__':
    client_socket = socket.socket()

    host = '127.0.0.1'
    port = 9999

    client_socket.connect((host, port))
    massage = input('Please input a string: ')
    client_socket.send(massage.encode('utf-8'))
    data = client_socket.recv(1024)
    print('recive data: ', data.decode())
    client_socket.close()
