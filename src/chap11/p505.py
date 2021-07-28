# abs() : 절대값
i = -20  
print(abs(i))
 
f = -30.92  
print(abs(f))


# all() : 모든 값이 참이면 True 반환. 0이 아닌 값은 True로 간주
mylist = [1, 3, 4, 6]  		 
print(all(mylist))      

mylist = [1, 3, 4, 0]  		
print(all(mylist))

mylist = [True, 0, False, 0]  	
print(all(mylist))


# any() : 한 개의 항목이라도 True이면 True를 반환
mylist = [0, 1, 2, 3]                              
print(any(mylist))	

mylist = [0, False]  
print(any(mylist))


# bin()  : 정수의 이진 표현을 반환
y = bin(64)  
print(y)  				


# eval() : 수식을 계산
exp = input("파이썬의 수식을 입력하시오: ")
print(eval(exp))

x = 10
y = 5
print(eval('x+y'))

x =  10  
print(eval('x + 1'))


# sum() : 합계
print(sum([1, 2, 3]))


# len() : 길이(갯수)
print(len("All's well that ends well. "))

print(len([1, 2, 3, 4, 5]))


# list() : 리스트를 생성
s  = 'abcdefg'       
print(list(s))
  
t = (1, 2, 3, 4, 5, 6)  
print(list(t))


# map() : 반복가능한 객체(리스트, 튜플 등)의 각 항목에 주어진 함수를 적용한 후 결과를 반환
def square(n):  
  return n*n  
  
mylist = [1, 2, 3, 4, 5]  
result = list(map(square, mylist))
print(result)  


# dir: 객체가 가지고 있는 변수나 함수를 출력
print(dir([1, 2, 3]))


# complex : 복소수 객체 real+imag*j를 생성
print(complex(4, 2))


# max(), min()
values = [ 1, 2, 3, 4, 5]
print(max(values))
print(min(values))


# enumerate() : 열거형 객체 (번호, 값)형식으로 반환
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))


# filter() : 특정조건(첫번째 인수)에 해당하는 요소만을 반환
def myfilter(x):  
	return x > 3  

result = filter(myfilter, (1, 2, 3, 4, 5, 6))  
print(list(result)) 


# zip() : 두개의 리스트를 1:1로 대응하면서 하나의 리스트로 결합
numbers = [1, 2, 3, 4]  
slist = ['one', 'two', 'three', 'four']  
print(list(zip(numbers, slist)))


names = [ "KIM", "LEE", "PARK" ]
scores = [ 100, 99, 80 ] 
for n, s in zip(names, scores):
	print(n, s)  

