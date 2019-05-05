#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket
import os


if __name__ == '__main__':
    server_socket = socket.socket()

    host = '127.0.0.1'
    port = 9999

    server_socket.bind((host, port))
    server_socket.listen(5)

    root_path = "/home/whether/桌面/python/"
    print('[info] server init complete...')
    while True:
        print('[info] wait for connect...')
        connect_socket, address = server_socket.accept()
        print('[info] Get connection from %s:%s' % address)
        while True:
            message = connect_socket.recv(1024).decode('utf-8')

            if message == 'get filename_list':
                print('[info] From [%s:%s] recive message: get filename_list' % address)
                filename_list = os.listdir(root_path)
                filename_str = ''.join([i+',' for i in filename_list])
                connect_socket.send(filename_str.encode('utf-8'))
                print('[info] send filename list complete!')

                filename = connect_socket.recv(1024).decode('utf-8')
                print('[info] From [%s:%s] recive filename: %s' % (address[0], address[1], filename))

                with open(root_path + filename, 'rb') as f:
                    passage = f.read()
                    connect_socket.send(passage)
                print('[info] send %s complete !' % filename)
            if message == 'quit':
                print('[info] From [%s:%s] recive message: quit' % address)
                break
        print('[info] [%s:%s] quit successful\n\n\n' % address)
        connect_socket.close()

