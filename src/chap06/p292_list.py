#1
# 6x5 2차원 배열 만들기. 리스트 함축
matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)

#2
# 2차원 리스트를 1차원 리스트로 만들기(1) - 리스트 함축
matrix = [ [0, 0, 0],     [1, 1, 1],     [2, 2, 2] ]
result = [num for row in matrix for num in row]
print(result)

#3 
# 2차원 리스트를 1차원 리스트로 만들기(2) - 반복문
matrix = [ [0, 0, 0],     [1, 1, 1],     [2, 2, 2] ]
result = []
for row in matrix:
     for num in row:
         result.append(num)
print(result)
