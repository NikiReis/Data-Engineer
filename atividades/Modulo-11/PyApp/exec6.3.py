class Television:

    CHANNEL_LIST = [2, 4, 6, 8, 10, 12, 16, 17, 26, 28]

    def __init__(self):
        self.Channels = Television.CHANNEL_LIST
        self.isOn = False
        self.current_channel = 0

    def power(self):
        if self.isOn:
            print('\nTurning off the TV')
            self.isOn = False
        else:
            print('\nTurning on the TV')
            self.isOn = True
            self.display_channel()

    def channel_up(self):
        if self.isOn:
            try:
                self.current_channel += 1
                self.display_channel()

            except IndexError:
                self.current_channel = 0
                self.display_channel()

        else:
            print('\nTurning on the TV')
            print(f"Channel {self.Channels[self.current_channel]}\n")
            self.isOn = True

    def channel_down(self):
        if self.On:
            try:
                self.current_channel -= 1
                print(f'\nChannel: {self.Channels[self.current_channel]}')

            except IndexError:
                self.current_channel = len(self.Channels) - 1
                self.display_channel()

        else:
            print('\nTurning on the TV')
            self.display_channel()
            self.isOn = True

    def display_channel(self):
        print(f"Channel: {self.Channels[self.current_channel]}")

    def run(self):
        while True:
            choice = str(input('\nTurn tv on/off [tv]\nUp channel [uc]\nDown channel [dc]\nExit infinity loop [0]')).lower()
            if choice == 'tv':
                self.power()
            elif choice == 'uc':
                self.channel_up()
            elif choice == 'dc':
                self.channel_down()
            elif choice == 'e':
                print('Exiting TV...')
                break
            else:
                print('Invalid input, please try again')


tv = Television()
tv.run()

