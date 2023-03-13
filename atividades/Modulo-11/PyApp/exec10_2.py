# Creating a personalized class of error
# In Python to force an exception we have to use the 'Raise' statement followed by the Exception Name
class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.Message = message


while True:
    try:
        x = int(input('Type a value between 0 and 10: '))
        if x > 10 or x < 0:
            raise InputError('Value is out of range. The value has to be between 0 and 10!')
        break
    except ValueError:
        print('Invalid value. Please, type only numeric values!! ')
    except InputError as ex:
        print(ex)
    # except range(x < 0) or (x > 10):
    #     print('Out of range')
