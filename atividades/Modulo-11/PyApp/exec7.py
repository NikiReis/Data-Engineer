# from exec6_3 import Television
from exec6_2 import Calculator
from exec7_2 import letter_counter, test


# tv = Television()
# tv.run()

if __name__ == '__main__':
    call = Calculator
    print(call.multiply(7, 8))
    list = ['Linek', 'Silva', 'Castro', 'Dos', 'Santos']
    print(letter_counter(['Linek', 'Silva', 'Castro', 'Dos', 'Santos']))
    print(f'Quantity of letter by words: Words: {list} : {letter_counter(list)}')
    print(test())
