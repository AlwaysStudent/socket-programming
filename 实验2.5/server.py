#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket
import threading


def init_server(host, port):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('[info] server init complete')
    return server_socket


def recv_message(connect_socket, connect_hostname):
    print('recv_message start:')
    while True:
        message = connect_socket.recv(1024).decode('utf-8')
        print('\n[%s] ' % connect_hostname, end='')
        print(message)


def send_message(connect_socket, hostname):
    print('send_message start:')
    while True:
        message = input('[%s] ' % hostname)
        connect_socket.send(message.encode('utf-8'))


def main():
    hostname = 'server-1'
    # hostname = input('Please input hostname:')

    server_host = '127.0.0.1'
    server_port = 9999
    server_socket = init_server(server_host, server_port)
    connect_socket, (connect_host, connect_port) = server_socket.accept()
    print("[info] connect from [%s:%s]" % (connect_host, connect_port))
    connect_socket.send(hostname.encode('utf-8'))
    connect_hostname = connect_socket.recv(1024).decode('utf-8')
    print('connect hostname: %s' % connect_hostname)

    t1 = threading.Thread(target=send_message, args=(connect_socket, hostname))
    t2 = threading.Thread(target=recv_message, args=(connect_socket, connect_hostname))
    t2.start()
    t1.start()
    t1.join()
    t2.join()

    connect_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()


