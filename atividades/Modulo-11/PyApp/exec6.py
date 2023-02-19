
def sumn(a, b):
    return a + b


print(sumn(4, 5))


def subtraction(a, b):
    return a - b


print(subtraction(3, 8))


class Calculator:
    def __init__(self, value1: int, value2: int):
        self.Value1 = value1
        self.Value2 = value2

    def sum(self):
        return self.Value1 + self.Value2

    def subtraction(self):
        return self.Value1 - self.Value2

    def multiply(self):
        return self.Value1 * self.Value2


while True:
    a = int(input('Type a value: '))
    b = int(input('Type another value: '))
    choice = str(input('Sum [s] / Multiply [m] / Subtract [sb]/ Close calculator [0]: '))
    call = Calculator(a, b)

    if choice == 's':
        print(call.sum())
    elif choice == 'm':
        print(call.multiply())
    elif choice == 'sb':
        print(call.subtraction())
    elif choice == '0':
        break
    else:
        print('Invalid input, try again: ')
