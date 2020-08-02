from tkinter import *
win = Tk()

btn1 = Button(win, text='left')
btn1.pack(side="left")
btn2 = Button(win, text='right')
btn2.pack(side="right", expand=True, fill='x')

win.mainloop()