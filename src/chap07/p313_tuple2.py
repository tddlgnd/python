#1 다른 튜플에 합치는 것은 가능
fruits = ("apple", "banana", "grape")
fruits += ("pear", "kiwi")
print(fruits)


#2 튜플 안의 리스트는 변경할 수 있다.
student = ("Kim", [3.1, 3.6, 4.0, 0.0])
student[1][3] = 4.3
print(student)

#3 +=연산자로 리스트에 튜플을 추가하는 것은 가능
numbers = [10, 20, 30]
numbers += (40, 50)  
# numbers = numbers + (40, 50)
print(numbers)
