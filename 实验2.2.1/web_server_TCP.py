#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket
import threading


def init_serversocket(host, port):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    return server_socket


def run(server_socket):
    while True:
        connect_socket, address = server_socket.accept()
        connect_host, connect_port = address
        t = threading.Thread(target=deal_with_client, args=(connect_socket, connect_host, connect_port))
        t.start()


def deal_with_client(connect_socket, connect_host, connect_port):
    request = connect_socket.recv(1024).decode('utf-8')
    print('[info] connect by [%s:%s]' % (connect_host, connect_port))
    request_path = request.split(' ')[1]
    response = ''
    if request_path == '/':
        request_file = '/index.html'
        with open('./website' + request_file, 'r') as response_file:
            response = 'HTTP/1.1 200 OK\r\n\r\n' + response_file.read()
    else:
        pass
    connect_socket.send(response.encode())
    connect_socket.close()


def main():
    host = '127.0.0.1'
    port = 8888
    server_socket = init_serversocket(host, port)
    run(server_socket)


if __name__ == '__main__':
    main()

