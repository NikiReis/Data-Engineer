import hashlib

message = input('Type the message that you want to encrypt: ')

while 1:
    try:
        hashtype = int(input('Which crytography do you want to choose: [1] - MD5\n[2] - SHA1\n[3] - SHA256\n[4] - SHA512\n[5] - SHA384'))
    except ValueError:
        print('Error')
    else:
        break

nwhash = hashlib.md5(b'Creating our first hash generator using MD5 algorithm')
print(nwhash.hexdigest())

