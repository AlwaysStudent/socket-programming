#!/usr/bin/python
# -*- coding = utf-8 -*-
import socket


def main():
    client_socket = socket.socket(type=socket.SOCK_DGRAM)

    host = '127.0.0.1'
    port = 9999

    while True:
        command = input('['+host+':'+str(port)+']$ ')
        if command == 'quit':
            break
        client_socket.sendto(command.encode('utf-8'), (host, port))
        message, (connect_host, connect_port) = client_socket.recvfrom(2048)
        message = message.decode('utf-8')
        print(message)

    client_socket.close()


if __name__ == '__main__':
    main()
