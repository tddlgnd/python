# 리스트 안에 서로 다른 정수의 갯수 구하기
list1 =[1,2,3,4,5,1,2,4 ]
print(len(set(list1)))


# 두개의 리스트에 공통적으로 들어 있는 숫자 구하기
list1 =[1,2,3,4,5 ]
list2 =[3,4,5,6,7 ]
print(set(list1)&set(list2))