from tkinter import *
window = Tk()

Button(window, text="박스 #1", bg="red", fg="white").pack()
Button(window, text="박스 #2", bg="green", fg="black").pack()
Button(window, text="박스 #3", bg="orange", fg="white").pack()

# 박스 배치 방향을 지정하려면 side= 사용
Button(window, text="박스 #1", bg="red", fg="white").pack(side=LEFT)
Button(window, text="박스 #2", bg="green", fg="black").pack(side=LEFT)
Button(window, text="박스 #3", bg="orange", fg="white").pack(side=RIGHT)

window.mainloop()