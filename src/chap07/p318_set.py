#1 세트 안에 자료의 개수
fruits ={"apple","banana","grape"}
size =len(fruits) 
print(size)


#2 어떤 항목이 세트 안에 있는지를 검사하려면 in 연산자 사용
fruits = { "apple", "banana", "grape" }
if "apple" in fruits:
	print("집합 안에 apple이 있습니다.")
    
    
#3 for 반복문을 이용하여 각 항목에 접근할 수 있다. 순서없이 출력   
fruits ={"apple","banana","grape"}
for x in fruits:
	print(x, end=" ")
print()
    

#4 정렬을 한 후 출력한다.    
fruits ={"apple","banana","grape"}
for x in sorted(fruits):
	print(x, end=" ")
