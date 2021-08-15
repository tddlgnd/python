#1 반복가능한 객체(리스트, 튜플)을 받아서 각 요소의 (인덱스, 값)형태의 튜플을 반환
fruits =["apple","banana","grape"]
for index, value in enumerate(fruits):
	print(index, value)


#2 enumerate()가 반환한 결과가 튜플임을 확인해보기 위해 리스트에 담아서 출력
fruits =["apple","banana","grape"]
result =list(enumerate(fruits))
print(result)
