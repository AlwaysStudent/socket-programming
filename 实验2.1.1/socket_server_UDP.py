#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


if __name__ == '__main__':
    server_socket = socket.socket(type=socket.SOCK_DGRAM)

    host = '127.0.0.1'
    port = 9999

    server_socket.bind((host, port))

    while True:
        data, address = server_socket.recvfrom(1024)
        data = data.decode('utf-8').upper()
        print('recive: ', data)
        server_socket.sendto(data.encode('utf-8'), address)

    server_socket.close()
