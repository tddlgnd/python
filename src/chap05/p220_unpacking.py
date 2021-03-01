# 리스트를 언패킹하여 print()에 전달하므로 개별 데이터 단위로 처리
alist = [ 1 , 2 , 3 ] 
print(*alist)


# 리스트를 전달하므로 리스트 단위로 처리
alist = [ 1 , 2 , 3 ] 
print(alist)


#인수를 언패킹하여 전달하므로 매개변수는 3개로 준비
def sum(a, b, c):
	print(a + b + c)

alist = [1, 2, 3]
sum(*alist)
