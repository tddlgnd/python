from tkinter import *

window = Tk()
f = Frame(window)

b1 = Button(f, text="박스 #1", bg="red",    fg="white")  #버튼을 프레임에 담아둔다
b2 = Button(f, text="박스 #2", bg="green",  fg="black")
b3 = Button(f, text="박스 #3", bg="orange", fg="white")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l = Label(window, text="이 레이블은 버튼들 위에 배치된다.")
l.pack()   #레이블을 윈도우에 배치

f.pack()   #프레임을 윈도우에 배치

window.mainloop()