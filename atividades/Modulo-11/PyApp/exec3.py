
for x in range(1, 101):
    if x % 2 != 0 or x <= 2:
        print(x)

n = int(input("Type a value: "))
div = 0
for x in range(1, n+1):
    rest = n % x
    if rest == 0:
        div += 1

if div == 2:
    print(f' Number {n} is prime')
else:
    print(f'Number {n} isn\'t prime ')


for num in range(101):
    div = 0
    for x in range(1, num):
        rest = num % x

        if rest == 0:
            div += 1

    if div == 2:
        print(num)

a = 0
while a <= 10:
    print(a)
    a += 1

note = int(input('Type the note: '))
while note > 10:
    note = int(input('Something\'s wrong, type the note again: '))
print(note)
