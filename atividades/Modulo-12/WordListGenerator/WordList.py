import itertools

result = itertools.permutations('admin', 5)

for i in result:
    print(''.join(i))


word = input('Type the string to be permuted: ')

new_result = itertools.permutations(word, len(word
                                              ))

for i in new_result:
    print(''.join(i))
