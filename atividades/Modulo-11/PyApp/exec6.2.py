class Calculator:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def multiply(self,valor_a, valor_b):
        return valor_a * valor_b

    def subtract(self, valor_a, valor_b):
        return valor_a - valor_b

    def division(self,valor_a, valor_b):
        return valor_a / valor_b


calcula = Calculator()
print(calcula.soma(10, 2))
print(calcula.multiply(5, 3))
print(calcula.subtract(7, 9))
print(calcula.division(3, 9))
