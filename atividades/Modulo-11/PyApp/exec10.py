lista = [1, 10]
archive = open('notas.txt')

try:
    text = archive.read()
    number = lista[1]
    divisao = 10 / 0

    # This piece of code below won't happen, because we had an error above us, we are trying to divide a number by 0
    # So when we are using the 'try' statement if we have an error, the rest of the code that is below that error won't
    # work
    # So the archive will remain opened, to prevent those or other kinds of errors we use the 'finally' statement to grantee that
    # the code will be executed, no matter if an error will occur or not

    # archive.close()
    print("Closing archive")

    # x = a
except ZeroDivisionError:
    print('Is impossible to do a division by zero')
except IndexError:
    print('Invalid index in the list')
except NameError:
    print('Variable not found')
except BaseException as e:
    print(f'Unknown error: {e}')
else:
    print('Executes when code doesn\'t lead us to an error or exception')
    print(divisao)
finally:
    print('Always execute')
    print('Closing the archive')
    archive.close()
