#################
### LISTING 38 
#################
import tkinter 
import random

def handle_key(event):                    #A
    if event.char == 'w' :                #B
        player1.move("u")                 #C
    if event.char == 's' :
        player1.move("d")
    if event.char == 'a' :
        player1.move("l")
    if event.char == 'd' :
        player1.move("r")
    if event.char == 'i' :                 #D
        player2.move("u")                  #E
    if event.char == 'k' :
        player2.move("d")
    if event.char == 'j' :
        player2.move("l")
    if event.char == 'l' :
        player2.move("r")
        
    yellow_xy = canvas.bbox(1)                                          #A
    overlapping = canvas.find_overlapping(
                   yellow_xy[0],yellow_xy[1],yellow_xy[2],yellow_xy[3]) #B
    if 2 in overlapping:                                                #C
        canvas.create_text(100,100,font=("Arial",20),text="Tag!")       #D        

class Player(object):
    def __init__(self, canvas, color):
        size = random.randint(1,100)
        x1 = random.randint(100,700)
        y1 = random.randint(100,700)
        x2 = x1+size
        y2 = y1+size
        self.color = color
        self.coords = [x1, y1, x2, y2]
        self.piece = canvas.create_rectangle(self.coords, tags=color)
        canvas.itemconfig(self.piece, fill=color)

    def move(self, direction):                           #A
        if direction == 'u':                             #B
            self.coords[1] -= 10                         #C
            self.coords[3] -= 10                         #C
            canvas.coords(self.piece, self.coords)       #D
        if direction == 'd':
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)
        if direction == 'l':
            self.coords[0] -= 10
            self.coords[2] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'r':
            self.coords[0] += 10
            self.coords[2] += 10
            canvas.coords(self.piece, self.coords)        
        
window = tkinter.Tk()
window.geometry("800x800")
window.title("태그!")
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill='both')

player1 = Player(canvas, "yellow")
player2 = Player(canvas, "blue")
canvas.bind_all('<Key>', handle_key)           #F

window.mainloop()
