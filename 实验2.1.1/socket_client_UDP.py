#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


if __name__ == '__main__':
    client_socket = socket.socket(type=socket.SOCK_DGRAM)

    host = '127.0.0.1'
    port = 9999

    massage = input('Please input a string: ')
    client_socket.sendto(massage.encode('utf-8'), (host, port))
    data, address = client_socket.recvfrom(1024)
    print('recive: ', data.decode('utf-8'))

    client_socket.close()