def letter_counter(words_list):
    counter = []
    for x in words_list:
        quantity = len(x)
        counter.append(quantity)
    return counter


def test():
    return 'Test'


if __name__ == '__main__':
    print(letter_counter(['Linek', 'Reis']))
