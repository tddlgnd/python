class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y 

    # +연산자와 print연산자를 재정의(연산자 오버로딩)하여 점과 점의 연산을 가능하게 구현
    # def __add__(self, other):
    #     x = self.x + other.x
    #     y = self.y + other.y
    #     return Point(x, y)
    
    # def __str__(self):
    #     return 'Point('+str(self.x)+', '+str(self.y)+')' 


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1+p2)