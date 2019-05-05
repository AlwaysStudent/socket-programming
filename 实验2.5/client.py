#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket
import threading


def init_client(host, port):
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print('[info] client init complete')
    return client_socket


def recv_message(client_socket, connect_hostname):
    print('recv_message start:')
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print('\n[%s] ' % connect_hostname, end='')
        print(message)


def send_message(client_socket, hostname):
    print('send_message start:')
    while True:
        message = input('[%s] ' % hostname)
        client_socket.send(message.encode('utf-8'))


def main():
    hostname = 'client-1'
    # hostname = input('Please input hostname:')

    client_host = '127.0.0.1'
    client_port = 9999
    client_socket = init_client(client_host, client_port)
    print("[info] connect to [%s:%d]" % (client_host, client_port))
    client_socket.send(hostname.encode('utf-8'))
    connect_hostname = client_socket.recv(1024).decode('utf-8')
    print('connect hostname: %s' % connect_hostname)

    t1 = threading.Thread(target=send_message, args=(client_socket, hostname))
    t2 = threading.Thread(target=recv_message, args=(client_socket, connect_hostname))
    t2.start()
    t1.start()
    t1.join()
    t2.join()

    client_socket.close()


if __name__ == '__main__':
    main()


