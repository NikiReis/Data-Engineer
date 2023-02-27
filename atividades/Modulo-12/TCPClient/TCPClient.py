import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print('Failed to connect!!')
        print(f'{error}')
        sys.exit()

    print('Socket was successfully created')

    targetHost = input('Type the host or IP to be connected: ')
    targetPort = input('Type the target port to be connected: ')

    try:
        connection.connect((targetHost, int(targetPort)))
        print(f'TCP client was successfully connected in the host: {targetHost} and in the port {targetPort}')
        connection.shutdown(2)
    except socket.error as error:
        print('Connection failed')
        print(f'Error:" {error}')
        sys.exit()


if __name__ == '__main__':
    main()
