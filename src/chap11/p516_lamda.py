# 1 lamda 형식의 함수를 사용
f = lambda x, y: x+y;

print("정수의 합 : ", f(10, 20))
print("정수의 합 : ", f(20, 20))


# 2 일반 함수를 사용
def get_sum(x, y):
    return x+y

print("정수의 합 : ", get_sum(10, 20))
print("정수의 합 : ", get_sum(20, 20))
