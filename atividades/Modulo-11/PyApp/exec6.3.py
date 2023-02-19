class Television:

    def __init__(self):
        self.Channels = [2, 4, 6, 8, 10, 12]
        self.On = False
        self.Pos = 0

    def power(self):
        if self.On:
            print('\nTurning off the TV')
            self.On = False
        else:
            print('\nTurning on the TV')
            print(f"Channel {self.Channels[self.Pos]}\n")
            self.On = True

    def channel_up(self):
        if self.On:
            try:
                self.Pos += 1
                print(f'\nChannel: {self.Channels[self.Pos]}')

            except IndexError:
                self.Pos = 0
                print(f'\nChannel: {self.Channels[self.Pos]}')

        else:
            print('\nTurning on the TV')
            print(f"Channel {self.Channels[self.Pos]}\n")
            self.On = True

    def channel_down(self):
        if self.On:
            try:
                self.Pos -= 1
                print(f'\nChannel: {self.Channels[self.Pos]}')

            except IndexError:
                self.Pos = len(self.Channels) - 1
                print(f'\nChannel: {self.Channels[self.Pos]}')

        else:
            print('\nTurning on the TV')
            print(f"Channel {self.Channels[self.Pos]}\n")
            self.On = True


tel = Television()

while True:

    op = str(input('\nTurn tv on/off [tv]\nUp channel [uc]\nDown channel [dc]\nExit infinity loop [0]')).lower()
    match op:
        case 'tv':
            tel.power()
        case 'uc':
            tel.channel_up()
        case 'dc':
            tel.channel_down()
        case '0':
            break
