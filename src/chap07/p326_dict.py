#1 딕셔너리 선언과 key와 value 출력
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"}
print(capitals.keys())
print(capitals.values())


#2 딕셔너리에서는 키가 있어야 값을 찾을 수 있다.
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
print(capitals["Korea"])	

#3 존재하지 않는 키를 제시하면 keyError 예외가 발생한다.
print(capitals["France"])	

#4 get() 또는 in을 사용하면 오류를 방지할 수 있다.
print(capitals.get("France", "해당 키가 없습니다."))

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
if "France" in capitals :
	print( "딕셔너리에 포함됨" )
else: 
	print( "딕셔너리에 포함되지 않음" )
