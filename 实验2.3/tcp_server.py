#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket
import time


def init_server(host, port):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('[info] server init complete')
    return server_socket


def return_time(connect_socket, connect_host, connect_port):
    now_time = time.strftime('%A, %B %d, %Y %H:%M:%S-%Z', time.localtime(time.time()))
    connect_socket.send(now_time.encode('utf-8'))
    print('[info] send time %s to [%s:%s]' % (now_time, connect_host, connect_port))


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
            return_time(connect_socket, connect_host, connect_port)
            message = connect_socket.recv(2048).decode('utf-8')
        if message == 'quit':
            connect_socket.close()
            print('[info] disconnect from [%s:%s]' % (connect_port, connect_host))


if __name__ == '__main__':
    main()
