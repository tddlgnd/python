#1 특정항목을 삭제하려면 pop() 사용. 삭제되는 항목은 반환된다.
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
city = capitals.pop("UK")
print(city)
print(capitals)


#2 주어진 키를 가진 항목이 없을 때 KeyError 에러 발생을 방지하려면 먼저 검사한 후 삭제
if "UK" in capitals :
	capitals.pop("UK")



#3 딕셔너리에 저장된 모든 키-값 쌍을 삭제하려면 clear() 사용
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 

capitals.clear()
print(capitals)
if len(capitals)==0 :
	print("딕셔너리가 비어 있음")
else:
	print("딕셔너리에 항목이 있음")

#------
#4 항목 방문하기(1) - 키들만 출력
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
        print( key, end=" ")

        
#5 항목 방문하기(2) - 키와 값 쌍을 출력 - 딕셔너리[키] 형식 사용       
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
        print( key,":", capitals[key])

        
#6 항목 방문하기(3) - 키와 값 쌍을 출력 - - items() 메소드 사용 
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key, value in capitals.items():
	print( key,":", value )        
    