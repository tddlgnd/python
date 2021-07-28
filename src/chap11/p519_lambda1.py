#1 람다식을 사용하지 않는 코드
def celsius(T):
    return (5.0/9.0)*(T-32.0)

f_temp = [0, 10, 20, 30, 40, 50]
c_temp = map(celsius, f_temp)
print(list(c_temp))


#2 람다식을 사용하는 코드
f_temp = [0, 10, 20, 30, 40, 50]
c_temp = map(lambda x: (5.0/9.0)*(x-32.0), f_temp)
print(list(c_temp))