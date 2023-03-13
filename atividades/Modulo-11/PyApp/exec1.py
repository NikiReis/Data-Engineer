# a = 10
# b = 5

a = int(input('Type the first value: '))
b = int(input('Type the second value: '))
soma = a+b
subtr = a-b
multiply = a*b
divisible = a/b

print(soma)
print(subtr)
print(multiply)
print(divisible)
rest = a%b
print('\n')

print('Sum: ',soma)
print('Substraction: ',subtr)
print('Multiply: ',multiply)
print('Division: ',divisible)

print('\n')
print(type(sum))
# typ = type(sum)
typ = str(soma)
print(typ)
print(str(soma))
print('Soma: ',typ)
typ2 = str(subtr)
print(int(typ2))
x = '1'
print(int(x)+1)

print('\n')

print('Sum: {}. Substraction: {}'.format(soma,subtr))
print(f'Sum: {soma}. SUbstraction: {subtr}.')

print('Sum: {soma}.\nSubstraction: {subtraction}.\n'
      'Multiplication: {multiply}.\n'
      'Division: {divisible}\n'
      'Rest: {rest}'.format(soma=soma,
                            subtraction=subtr,
                            multiply=multiply,
                            divisible=divisible,
                            rest=rest

    ))

