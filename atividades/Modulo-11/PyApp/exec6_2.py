class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def sum(valor_a, valor_b):
        return valor_a + valor_b

    @staticmethod
    def multiply(valor_a, valor_b):
        return valor_a * valor_b

    @staticmethod
    def subtract(valor_a, valor_b):
        return valor_a - valor_b

    @staticmethod
    def division(valor_a, valor_b):
        return valor_a / valor_b


if __name__ == '__main__':
    calculate = Calculator()
    print(calculate.sum(10, 2))
    print(calculate.multiply(5, 3))
    print(calculate.subtract(7, 9))
    print(calculate.division(3, 9))
