import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket client successfully created')
host = 'localhost'
port = 5433
message = 'Hello, server how\'s it going ? '
try:
    print('Client: ' + message)
    connection.sendto(message.encode(), (host, 5432))

    data, server = connection.recvfrom(4096)
    data = data.decode()
    print('Client: ' + data)
finally:
    print('Client: Closing connection')
    connection.close()
