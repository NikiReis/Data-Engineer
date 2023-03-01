import hashlib
from time import sleep


def printing_out():
    print('Printing the message encrypted')
    sleep(1)


class Error(Exception):
    pass


class OutOFIndex(Error):
    def __init__(self, messages):
        self.message = messages


message = input('Type the message that you want to encrypt: ')

while 1:
    try:
        hashtype = float(input('Which crytography do you want to choose\n[1] - MD5\n[2] - SHA1\n[3] - SHA256\n[4] - SHA512\n[5] - SHA384\n[0] - Exit Hash Generator\nSelect one of the list: '))

        if hashtype > 5 or hashtype < 0:
            raise OutOFIndex('Value out of index! Type a value between 0 and 5\n')
        break

    except ValueError:
        print('Wrong input. Only numeric input is acceptable\n')

    except OutOFIndex as err:
        print(err)


if hashtype == 1:
    printing_out()
    message = hashlib.md5(b'Creating our first hash generator using MD5 algorithm')
    print(message.hexdigest())

elif hashtype == 2:
    printing_out()
    message = hashlib.sha1(b'Creating our first hash generator using SHA1 algorithm')
    print(message.hexdigest())

elif hashtype == 3:
    printing_out()
    message = hashlib.sha256(b'Creating our first hash generator using SHA256 algorithm')
    print(message.digest())

elif hashtype == 4:
    printing_out()
    message = hashlib.sha512(b'Creating our first hash generator using SHA512 algorithm')
    print(message.digest())

elif hashtype == 5:
    printing_out()
    message = hashlib.sha384(b'Creating our first hash generator using SHA256 algorithm')
    print(message.digest())

elif hashtype == 0:
    print('Closing the Hash generator')

