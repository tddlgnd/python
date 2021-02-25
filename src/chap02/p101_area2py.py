SQMETER_PER_P = 3.3

area = eval(input ("면적(제곱미터):"))
py = area / SQMETER_PER_P
print("%.2f" % py, "평") 	# 출력 7.76 평

print("%10.2f" % py, "평") 	# 출력 7.76 평  (10자리 중에 소수점 아래 두자리)
print("평: %10.2f -> 제곱미터: %8.2f" % (py, area)) 	