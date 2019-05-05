#!/usr/bin/python
# -*- coding=utf-8 -*-
import socket


def init_client(host, port):
    client_socket = socket.socket()
    client_socket.connect((host, port))
    return client_socket


def display_filename_list(filename_str):
    filename_list = filename_str.split(',')
    for i in range(len(filename_list)):
        print('%16s' % filename_list[i], end='')
        if i % 3 == 2:
            print()


def deal_with_server(client_socket, working_path):
    hello_message = client_socket.recv(1024).decode('utf-8')
    print('[info] connect FTP server successfully')
    print('---%s---' % hello_message)
    filename_str = client_socket.recv(2048).decode('utf-8')
    display_filename_list(filename_str)
    while True:
        message = input('client >>')
        if message[0:2] == 'GET':
            get_file(client_socket, message, working_path)
        elif message[0:2] == 'PUT':
            put_file(client_socket, message, working_path)
        elif message[0:1] == 'CD':

        elif message == 'PWD':
            pwd(client_socket, working_path)
        elif message == 'QUIT':
            break


def get_file(client_socket, message, working_path):
    filename = message.split(' ')[1]
    recv_message = client_socket.recv(40960).decode('utf-8')
    if recv_message[:5] == '[info]':
        print(recv_message)
    else:
        with open(working_path + filename, 'wb') as f:
            f.write(recv_message)


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


def main():
    client_host = '127.0.0.1'
    client_port = 8888
    working_path = '/home/whether/桌面/计算机网络/socket_programming/实验2.6/ftp_client_working_path/'
    client_socket = init_client(client_host, client_port)
    while True:
        deal_with_server(client_socket, working_path)
