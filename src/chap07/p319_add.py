fruits = { "apple", "banana", "grape" }
print(fruits)

#add() 메소드를 이용하여 요소를 추가한다
fruits.add("kiwi")      	
print(fruits)


#remove() 메소드로 요소를 삭제한다.
fruits.remove("kiwi")   	
print(fruits)


#remove() 메소드는 삭제하고자 하는 요소가 없으면 오류를 생성한다.
#fruits.remove("mango")  	


#discard() 메소드는 삭제하고자 하는 요소가 없으면 그냥 넘어간다.
fruits.discard("mango") 	


#clear() 메소드는 세트의 모든 요소를 삭제한다.
fruits.clear()          	
print(fruits)


#세트에 여러개의 항목을 추가할 때에는 update() 메소드를 사용한다.
fruits = {"apple", "banana", "grape"}
fruits.update(["orange", "mango", "kiwi"])
print(fruits)
