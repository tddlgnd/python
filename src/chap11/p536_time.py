# 1
import time
print(time.time())

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
print(end-start)

# 3
import time
print(time.asctime())

# 4
import time
t = (2016, 4, 29, 12, 10, 50, 5, 0, 0)
print(time.asctime(t))

# 5
import time
for i in range(10, 0, -1):
    print(i, end=" ")
    time.sleep(1)
print("발사! ")
