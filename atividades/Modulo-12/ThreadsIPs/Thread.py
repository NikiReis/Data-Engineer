from time import sleep
from threading import Thread
"""
def car1(velocity):
    traject = 0

    while traject <= 100:
        print('car1: ', traject)
        traject += velocity

car1(10)


def car2(velocity):
    traject = 0

    while traject <= 100:
        print('car1: ', traject)
        traject += velocity

car2(20)
"""


def car(velocity, driver):
    traject = 0
    while traject <= 100:
        print(f'Driver: {driver}, Traject: {traject}')
        traject += velocity
        sleep(1)


car1 = Thread(target=car, args=[3,'Linek'])
car2 = Thread(target=car, args=[1, 'Someone else'])
car1.start()
car2.start()
