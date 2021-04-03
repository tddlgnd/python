heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치", "헐크" ]
n = heroes.index("헐크")		# n은 2가 된다. 
print(n)

if "헐크" in heroes:
    print(heroes.index("헐크"))

heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치", "헐크" ]
n = heroes.index("헐크", 3)		# 인덱스 3부터 찾기 시작. n은 4가 나온다. 
print(n)
