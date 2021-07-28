class Shape:
    def __init__(self, name):    
        self.name = name
    def getArea(self):
        raise NotImplementedError("이것은 추상메소드입니다. ")

class Circle(Shape):
    def __init__(self, name, radius):    
        super().__init__(name)
        self.radius = radius

    def getArea(self):             
        return  3.141592*self.radius**2

class Rectangle(Shape):
    def __init__(self, name, width, height):    
        super().__init__(name)
        self.width = width
        self.height = height

    def getArea(self):             
        return  self.width*self.height

shapeList = [Circle("c1", 10), Rectangle("r1", 10, 10)]

# 동일한 메소드를 호출하여도 자식 클래스에 따라 다르게 처리
for s in shapeList:
	print(s.getArea())
    
# #나머지 요소들을 출력
# for s in shapeList:
#     print(s.name)

# print(shapeList[0].name, shapeList[0].radius, shapeList[1].name, shapeList[1].width, shapeList[1].height )