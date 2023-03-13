import socket


connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket successfully created')
host = 'localhost'
port = 5432
connection.bind((host, port))
message = 'What\'s up client'

while 1:
    data, address = connection.recvfrom(4096)
    if data:
        print('Server is sending a message')
        connection.sendto(data + (message.encode()), address)
