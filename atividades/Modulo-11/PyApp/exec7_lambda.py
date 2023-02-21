letter_counter = lambda lists: [len(x) for x in lists]
lista = ['Linek', 'Dos', 'Reis']
print(letter_counter(lista))

counter = map(len, lista)
print(list(counter))

sum = lambda x, y: x + y
print(sum(7, 8))

calculator = {
    'Sum': lambda a, b: a + b,
    'Multiply': lambda a, b: a * b,
    'Subtraction': lambda a, b: a - b,
    'Division': lambda a, b: a // b
}

soma = calculator['Sum']
mult = calculator['Multiply']
div = calculator['Division']
sub = calculator['Subtraction']

if __name__ == '__main__':
    print(soma(9, 8))
    print(mult(9, 3))
    print(div(92, 6))
    print(sub(89, 36))
