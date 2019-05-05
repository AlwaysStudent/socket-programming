#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket
import time


def init_server(host, port):
    server_socket = socket.socket(type=socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    return server_socket


def return_time(server_socket, connect_host, connect_port):
    now_time = time.strftime('%A, %B %d, %Y %H:%M:%S-%Z', time.localtime(time.time()))
    server_socket.sendto(now_time.encode('utf-8'), (connect_host, connect_port))
    print('[info] send time %s to [%s:%s]' % (now_time, connect_host, connect_port))


def main():
    host = '127.0.0.1'
    port = 9999
    server_socket = init_server(host, port)
    while True:
        message, (connect_host, connect_port) = server_socket.recvfrom(2048)
        message = message.decode('utf-8')
        while message != 'quit':
            return_time(server_socket, connect_host, connect_port)
            message, (connect_host, connect_port) = server_socket.recvfrom(2048)
            message = message.decode('utf-8')
        if message == 'quit':
            server_socket.close()


if __name__ == '__main__':
    main()
