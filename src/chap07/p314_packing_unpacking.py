#1 
x = ("apple", "banana", "grape")     #튜플 패킹
print(x)
(s1, s2, s3) = x                     #튜플 언패킹
print(s1)
print(s2)
print(s3)


#2 서로 다른 자료형에 대해서도 패킹과 언패킹이 가능
student = ("Kim", [3.1, 3.6, 4.0, 0.0])   #패킹
name, grades = student                    #언패킹
print(name)
print(grades)


#3 패킹과 언패킹을 이용하여 데이터의 값을 바꿀 수 있다.
n1 = 10
n2 = 90
n1, n2 = (n2, n1)
print(n1)
print(n2)
