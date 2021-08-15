#1 클래스 안의 인스턴스 변수를 외부에서 변경할 수 있다. 
class Student:
	def __init__(self, name=None, age=0):
		self.name = name
		self.age = age

obj = Student("Hong", 20)
obj.age = 21
print(obj.age)



#2 클래스 안의 변수를 외부에서 변경할 수 없다. - 정보은익
class Student:
	def __init__(self, name=None, age=0):
		self.__name = name		# __가 변수 앞에 붙으면 외부에서 변경 금지
		self.__age = age			# __가 변수 앞에 붙으면 외부에서 변경 금지

obj=Student()
print(obj.__age)			# 오류 발생!
