#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


def init_server(host, port):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('[info] server init complete')
    return server_socket


def return_echo(connect_socket, message, connect_host, connect_port):
    connect_socket.send(message.encode('utf-8'))
    print('[info] send message [%s] to [%s:%s]' % (message, connect_host, connect_port))


def main():
    host = '127.0.0.1'
    port = 9999
    server_socket = init_server(host, port)
    while True:
        connect_socket, address = server_socket.accept()
        connect_host, connect_port = address
        print('[info] server connected by [%s:%s]' % (connect_host, connect_port))
        message = connect_socket.recv(2048).decode('utf-8')
        while message != 'quit':
            return_echo(connect_socket, message, connect_host, connect_port)
            message = connect_socket.recv(2048).decode('utf-8')
        if message == 'quit':
            connect_socket.close()
            print('[info] disconnect from [%s:%s]' % (connect_port, connect_host))


if __name__ == '__main__':
    main()
