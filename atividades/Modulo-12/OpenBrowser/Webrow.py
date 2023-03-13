from tkinter import *
import webbrowser

root = Tk()
root.title('Open browser')

root.geometry('700x480')

def firefox():
    webbrowser.open('youtube.com')


myyt = Button(root, text='Open Youtube', command=firefox).pack(pad=20)

root.mainloop()