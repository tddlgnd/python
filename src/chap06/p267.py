#1.  min(), max()를 사용한 방법
scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print("제거전", scores)
scores.remove(max(scores))
scores.remove(min(scores))
print("제거후", scores)

#2. 정렬을 이용하는 방법
scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print("제거전", scores)
scores.sort() 
print("정렬후", scores)

new_scores = scores[1:-1]    #score[1:-1]은 인덱스 1에서 인덱스 -1 직전까지를 의미한다.
print("제거후", new_scores)  

