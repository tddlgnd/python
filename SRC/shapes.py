class Circle(object):
    """ radius(반지름)을 가지는 원 객체 """    
    def __init__(self):
        self.radies = 0
        
    def change_radius(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
class Rectangle(object):
    """ length(길이)와 width(너비)를 가지는 직사각형 객체 """
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def set_length(self, length):
        self.length = length
    def set_width(self, width):
        self.width = width
