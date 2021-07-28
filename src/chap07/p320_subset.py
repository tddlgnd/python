#1 부분집합인지를 검사하려면 < 연산자나 issubset() 메소드를 사용
A ={"apple","banana","grape"}
B ={"apple","banana","grape","kiwi"}

if A < B : 			# 또는 A.issubset(B) :
	print("A는 B의 부분 집합입니다.")
    
    
#2 두개의 세트가 같은지는 ==, != 사용    
A ={"apple","banana","grape"}
B ={"apple","banana","grape","kiwi"}
if A == B :
	print("A와 B는 같습니다.")
else :
	print("A와 B는 같지 않습니다.")