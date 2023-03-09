import ctypes

attributes_hide = 0x02
directory = input('Type the directory that you want to hide ex: C:/pasta')
retturn = ctypes.windll.kernel32.SetFileAttributesW('filetobehide.txt', attributes_hide)

if retturn:
    print('File hided')
else:
    print('Impossible to hide')
