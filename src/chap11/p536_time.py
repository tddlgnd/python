# 1
import time
print(time.time())   #1970.1.1 이후부터 지금까지 흘러온 시간(초)


# 2
import time
def fib(n):    # 피보나치 수열 출력
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

start = time.time()
fib(1000)	
end = time.time()
print(end-start)    #실행시간을 측정


# 3
import time
print(time.asctime())   #현재 날짜와 시간을 문자열 형태로 출력


# 4
import time
t = (2016, 4, 29, 12, 10, 50, 5, 0, 0)   #(연, 월, 일, 시, 분, 초, 요일, 0, 0) 형식으로 날짜 지정
print(time.asctime(t))


# 5
import time
for i in range(10, 0, -1):
    print(i, end=" ")
    time.sleep(1)   #1초 동안 정지
print("발사! ")
