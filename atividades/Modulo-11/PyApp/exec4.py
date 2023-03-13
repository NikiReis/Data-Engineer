from math import *
import random

lisst = [1, 3, 5, 7, 13, 2, 9, 0, 21, 33, 76, 87]
animals = ['Dog', 'Cat', 'Elefant', 'Paraguaio', 'Butterfly', 'Lion', 'Jaguar']

print(lisst)

print(lisst[:7:2])
print(lisst[1:-3:3])
new_list = lisst + animals
n_list = lisst*2
print(new_list)

for x in range(len(new_list)):
    print(new_list[x])

for x in new_list:
    print(x)

print(pow(3, 2))
print(max(lisst))
print(sum(lisst))


print(max(animals))
print(min(animals))
print(random.choice(animals))
random.shuffle(animals)
print(animals)

for x in range(6):
    random.shuffle(animals)
    print(animals)

insert = str(input('Type an animal\'s name: '))


if insert in animals:
    print('There\'s a cat in the list')
else:
    print('This animal wasn\'t found. Including into the list')
    animals.insert(3, insert)
    print(animals)


if insert in animals:
    print('There\'s a cat in the list')
else:
    print('This animal wasn\'t found. Including into the list')
    animals.append(insert)
    print(animals)

# tupla = tuple() or tupla = ()
tupla = ('Knife', 'Spoon', 'Fork')
print(tupla[-2])
print(len(tupla))
print(len(animals))
tup = tuple(animals)
print(type(animals))
print(type(tup))
