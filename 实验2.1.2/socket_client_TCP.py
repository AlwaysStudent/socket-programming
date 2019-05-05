#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


if __name__ == '__main__':
    client_socket = socket.socket()

    host = '127.0.0.1'
    port = 9999

    client_socket.connect((host, port))
    print('[info] connection to %s:%d' % (host, port))
    print('[info] connection successful')

    message = 'file'
    print('[info] To [%s:%d] send message: get filename_list' % (host, port))
    client_socket.send(message.encode('utf-8'))
    print('[info] send message complete')
    filename_list = client_socket.recv(1024).decode('utf-8').split(',')
    filename_list.pop()
    print('[info] From [%s:%d] recive message: filename_list')
    print('This DIR:')
    count = 0
    for i in filename_list:
        print('%16s' % i, end='')
        count = count + 1
        if count % 3 == 0:
            print('')

    filename = input("\n\n[info] Please input the filename:\n")

    while filename not in filename_list:
        print('[info] filename error!')
        filename = input("\n[info] Please input the filename:\n")

    client_socket.send(filename.encode('utf-8'))
    print('[info] filename send complete!')
    file = client_socket.recv(102400)
    with open(filename, 'wb') as f:
        f.write(file)
    print('[info] Dowdload file complete !')
    client_socket.send('quit'.encode('utf-8'))

    client_socket.close()
