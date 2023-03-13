import hashlib

file1 = 'message.txt'
file2 = 'newmessage.txt'

hash1 = hashlib.new('md5')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('md5')

hash2.update(open(file2, 'rb').read())

if hash2.digest() != hash1:
    print('Their different')
    print(f'Hash 1 {hash1.hexdigest()}\nHash 2: {hash2.hexdigest()}')
else:
    print(f'They\'re pretty much the same')
