import math

class Shape:
     def __init__(self):
        pass

     def draw(self):
        print("draw()가 호출됨")

class Circle(Shape):
     def __init__(self, radius=0):
        super().__init__()
        self.radius = radius
 
     def draw(self): 
        super().draw()      #부모 클래스의 draw()가 호출된다.
        print("원을 그립니다.")

c = Circle(10)
c.draw()