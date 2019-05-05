#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket
import os


class TCP_server:
    """
    A class for easy TCP server
    """
    def __init__(self, host, port, working_path):
        self.server_socket = socket.socket()
        self.host = host
        self.port = port
        self.working_path = working_path
        self.server_init()
        while True:
            self.run()

    def server_init(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print('[info] server init complete...')

    def run(self):
        print('[info] wait for connect...')
        connect_socket, connect_address = self.server_socket.accept()
        print('[info] Get connection from %s:%s' % connect_address)
        while True:
            first_message = connect_socket.recv(1024).decode('utf-8')
            if first_message == 'upper':
                self.upper_word(connect_socket)
            elif first_message == 'file':
                self.send_file(connect_socket, self.working_path)
            elif first_message == 'quit':
                self.quit_connect(connect_address)
                break
            else:
                print('[info] error command!')
                connect_socket.send('quit_by_error'.encode('utf-8'))
                break
        connect_socket.close()

    def upper_word(self, connect_socket):
        passage = connect_socket.recv(1024).decode('utf-8').upper()
        connect_socket.send(passage.encode('utf-8'))
        print('[info] upper word send complete!')

    def send_file(self, connect_socket, working_path):
        filename_list = os.listdir(working_path)
        filename_str = ''.join([i + ',' for i in filename_list])
        connect_socket.send(filename_str.encode('utf-8'))
        print('[info] send filename list complete!')

        filename = connect_socket.recv(1024).decode('utf-8')

        with open(working_path + filename, 'rb') as f:
            passage = f.read()
            connect_socket.send(passage)
        print('[info] send %s complete !' % filename)

    def quit_connect(self, connect_address):
        print('[info] [%s:%s] quit successful\n\n\n' % connect_address)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999
    working_path = "/home/whether/桌面/python/"
    TCP_server(host, port, working_path)
