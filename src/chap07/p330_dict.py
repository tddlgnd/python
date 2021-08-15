#1 values 리스트에서 x가 짝수이면 x**2를 계산하여 딕셔너리 생성
values =[1,2,3,4,5,6] 

dic ={ x : x**2 for x in values if x%2==0 }
print(dic)


#2 리스트에서 숫자를 키로, 문자열로 변환한 것을 값으로 사용하여 딕셔너리 생성
dic ={ i:str(i)for i in [1,2,3,4,5]}
print( dic )


#3 리스트에서 문자열을 키로, 문자열의 길이를 값으로 사용하여 딕셔너리 생성
fruits =["apple","orange","banana"]
dic ={ f :len(f)for f in fruits }
print( dic )


#4 딕셔너리에서 값을 키로, 키를 값으로 딕셔너리 생성
dic1 ={"One":1,"Two":2,  "Three":3 }
dic2 ={ n : w for w , n in dic1.items()}
print( dic2 )