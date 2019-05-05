#!/usr/bin/python
# -*- coding=utf-8 -*-
import socket
import threading
import os


def send_filename_list(connect_socket, working_path):
    filename_list = os.listdir(working_path)
    filename_bit = ''.join([i + ',' for i in filename_list])[:-1].encode('utf-8')
    connect_socket.send(filename_bit)


def deal_with_client(connect_socket, working_path):
    connect_socket.send('Hello, welcome to connect FTP server'.encode('utf-8'))
    send_filename_list(connect_socket, working_path)
    os.chdir(working_path)
    while True:
        message = connect_socket.recv(1024).decode('utf-8')
        if message[0:2] == 'GET':
            get_file(connect_socket, message, os.getcwd())
        elif message[0:2] == 'PUT':
            put_file(connect_socket, message, os.getcwd())
        elif message[0:1] == 'CD':
            os.chdir(cd(connect_socket, message, os.getcwd()))
        elif message == 'PWD':
            pwd(connect_socket, os.getcwd())
        elif message == 'QUIT':
            break
    connect_socket.close()


def get_file(connect_socket, message, working_path):
    filename = message.split(' ')[1]
    filename_list = os.listdir(working_path)
    if filename not in filename_list:
        connect_socket.send('[info] wrong filename'.encode('utf-8'))
    else:
        with open(working_path+filename, 'rb') as f:
            passage = f.read()
            connect_socket.send(passage)


def put_file(connect_socket, message, working_path):
    filename = message.split(' ')[1]
    filename_list = os.listdir(working_path)
    passage = connect_socket.recv(409600)
    if filename in filename_list:
        os.remove(working_path+filename)
    os.mknod(filename)
    with open(working_path + filename, 'wb') as f:
        f.write(passage.decode('utf-8'))


def cd(connect_socket, message, working_path):
    os.chdir(working_path)
    path = message.split(' ')[1]
    os.chdir(path)
    send_filename_list(connect_socket, working_path)
    return os.getcwd()


def pwd(connect_socket, working_path):
    connect_socket.send(working_path.encode('utf-8'))


def init_server(host, port):
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    return server_socket


def main():
    server_host = '127.0.0.1'
    server_port = 8888
    working_path = '/home/whether/桌面/计算机网络/socket_programming/实验2.6/ftp_server_working_path/'
    server_socket = init_server(server_host, server_port)
    while True:
        connect_socket, (connect_host, connect_port) = server_socket.accept()
        print('[info] connect from [%s:%s]' % (connect_host, connect_port))
        t1 = threading.Thread(target=deal_with_client, args=(connect_socket, working_path))
        t1.start()
        t1.join()


if __name__ == '__main__':
    main()
