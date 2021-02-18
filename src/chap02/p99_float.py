# 1
SQMETER_PER_P = 3.3

area = float(input ("면적(제곱미터):"))
py = area / SQMETER_PER_P
print(py, "평")


# 2  eavl() 함수를 사용하여도 된다.
SQMETER_PER_P = 3.3

area = eval(input ("면적(제곱미터):"))
py = area / SQMETER_PER_P
print(py, "평")