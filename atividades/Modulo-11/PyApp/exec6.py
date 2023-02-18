
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

    def sumn(self):
        return self.Value1 + self.Value2

    def substrac(self):
        return self.Value1 - self.Value2

    def multiply(self):
        return self.Value1 * self.Value2


while True:
    a = int(input('Type a value: '))
    b = int(input('Type another value: '))
    op = str(input('Sum [s] / Multiply [m] / Subtract [sb]/ Close calculator [0]: '))

    cal = Calculator(a, b)

    match op:
        case 's':
            print(cal.sumn())
        case 'm':
            print(cal.multiply())
        case 'sb':
            print(cal.substrac())
        case '0':
            break
