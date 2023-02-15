e = int(input('Type the first note: '))
r = int(input('Second note: '))
t = int(input('Third note: '))
p = int(input('Fourth note'))

avg = (e+r+t+p)/4
print(f'Average: {avg}')

if e <= 10 and r <= 10 and t <= 10 and p <= 10:
    print(f'Student\'s average note: {avg}')
else:
    print('Something\'s wrong, try to type the notes again')

x = int(input('First value: '))
y = int(input('Second Value: '))

rest_x = x % 2
rest_y = y % 2

if rest_x == 0 or not rest_y > 0:
    print('A pair number was typed')
else:
    print('Only odds numbers were typed')

    a = int(input('First value: '))
    b = int(input('Second value: '))
    c = int(input('Third value: '))

    if a > b and a > c:
        print(f'The greater value is: {a}')
    elif b > a and b > c:
        print(f'The greater value is {b}')
    else:
        print(f'The greater value is {c}')

    print('End of the program')
