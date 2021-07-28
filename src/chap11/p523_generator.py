# 반목가능한 객체 10개를 생성. 제너레이터
def MyCounterGen(low, high):
    while low <= high:
       yield low
       low += 1

# 먼저 MyCounterGen()으로 반복가능한 객체(이터레이터 객체)를 만든 후에 for로 반복(이터레이터)
for i in MyCounterGen(1, 10):
    print(i, end=' ')