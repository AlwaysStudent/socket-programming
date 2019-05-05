#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


if __name__ == '__main__':
    server_socket = socket.socket()

    host = '127.0.0.1'
    port = 9999

    server_socket.bind((host, port))
    server_socket.listen(5)
    while True:
        connect_socket, address = server_socket.accept()
        print(connect_socket, address)
        while True:
            try:
                data = connect_socket.recv(1024)
                print('recive: ', data.decode('utf-8'))
                connect_socket.send(data.upper())
                break
            except ConnectionResetError as error:
                print('Close the process in way!')
                break
        connect_socket.close()
