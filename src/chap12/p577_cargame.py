from tkinter import *
import random

# Canvas 클래스를 상속받아서 Car 클래스를 정의한다.  
class Car(Canvas): 
    def __init__(self, master = None):   #캔버스를 생성하고 자동차를 그린다.
        Canvas.__init__(self, master, width = 500, height = 70)  
        self.master = master 
        self.dx = 0
        self.dy = 0
        self.rectangle = self.create_rectangle(0, 5, 70, 35, fill = "black") 
        self.oval = self.create_oval(5, 20, 25, 50, fill = "black") 
        self.oval2 = self.create_oval(40, 20, 60, 50, fill = "black") 
        self.pack() 
        self.movement() 
      
    def movement(self):    #자동차 객체를 (dx, 0)만큼 움직인다.
        dx = random.randint(2, 10)
        self.move(self.rectangle, dx, 0) 
        self.move(self.oval, dx, 0) 
        self.move(self.oval2, dx, 0) 
        self.after(100, self.movement)   #100ms 후에 메소드를 다시 호출
      
master = Tk() 
car1 = Car(master) 
car2 = Car(master) 
car3 = Car(master)   
mainloop()