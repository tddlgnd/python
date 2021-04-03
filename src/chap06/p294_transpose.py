#전치행렬 구하기(1) : 중첩된 for 루프 이용 
transposed = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("원래 행렬=", matrix)
# 열의 개수만큼 반복한다. 
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:		# 행렬의 각 행에 대하여 반복
        #print(row)
        #print(row[i])
        transposed_row.append(row[i])	# i번째 요소를 row에 추가한다. 
    transposed.append(transposed_row)

print("전치 행렬=", transposed)


#전치행렬 구하기(2) : 리스트 함축 이용
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("원래 행렬=", matrix)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("전치 행렬=", transposed)
