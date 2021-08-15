class Animal(object):
    pass

class Dog(Animal):          #Dog 클래스와 Animal 클래스의 관계는 is-a
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

dog1 = Dog("dog1")
person1 = Person("홍길동")
person1.pet = dog1         #Person 클래스와 Dog 클래스의 관계는 has-a
