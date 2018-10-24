from tkinter import *
from tkinter.messagebox import *

root = Tk()

global hi
hi = 'hello there'
def clicked():
    showinfo(message = hi)
    
boo = Label(master = root, text = 'HELLO Gooey', relief = GROOVE)
button = Button(root, text='\'Sup?', command = clicked)
entry = Entry(root)
entry.pack()
button.pack(side=BOTTOM)
boo.pack(side=TOP)
root.mainloop()
