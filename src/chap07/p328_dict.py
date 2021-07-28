#1 키와 값을 일대일로 추가
capitals = {"Korea":"Seoul","USA":"Washington","UK":"London"} 
capitals["France"] = "Paris"
print(capitals)


#2 처음에 공백 딕셔너리를 생성하고 여기에 하나씩 항목을 추가
capitals = {}
capitals["Korea"]="Seoul"
capitals["USA"]="Washington"
capitals["UK"]="London"
capitals["France"]="Paris"
print(capitals)


#3 다른 딕셔너리 전체를 현재 딕셔너리에 추가하고 싶으면 update()를 사용
capitals = {"Korea":"Seoul","USA":"Washington","UK":"London"} 
capitals.update({"France":"Paris","Germany":"Berlin"})
print(capitals)