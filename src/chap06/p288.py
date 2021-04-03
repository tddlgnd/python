#1
# 동적으로 2차원 리스트를 생성한다. 
rows = 3
cols = 5

s = [ ]
for row in range(rows): 
	s += [[0]*cols]		# 2차원 리스트끼리 합쳐진다. 

print("s =", s)


#2
# 주의 : 리스트로 더하지 않으면 1차원 리스트가 되어 버린다.
rows = 3
cols = 5

s = [ ]
for row in range(rows): 
	s += [0]*cols		# 1차원 리스트끼리 합쳐진다. 

print("s =", s)


#3 
# 리스트 함축을 사용하여 2차원 리스트를 생성한다.
rows = 3
cols = 5

s = [ ([0] * cols) for row in range(rows) ]

print("s =", s)
