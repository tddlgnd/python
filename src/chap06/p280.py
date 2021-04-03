#1. 값으로 호출하기 - 정수나 문자열처럼 변경이 불가능한 객체 
def func1(x):
    x = 42
    print( "x=",x," id=",id(x))

y = 10
func1(y)
print( "y=",y," id=",id(y))


#2. 참조값으로 호출하기 - 리스트처럼 변경 가능한 객체
def func2(list):
     list[0] = 99
 
values = [0, 1, 1, 2, 3, 5, 8]
func2(values)
print(values)
